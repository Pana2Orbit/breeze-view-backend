from fastapi import APIRouter, HTTPException
import torch
from pathlib import Path
import logging

import numpy as np

from app.models.requests import PredictionRequestModel
from app.models.responses import PredictionResponseModel
from app.core.ml.model import LSTMForecaster

router = APIRouter()
logger = logging.getLogger(__name__)

# Get the absolute path to the model file in the same directory as this file
MODEL_PATH = Path(__file__).parent / "lstm_forecaster_best.pt"

model = None

try:
    if MODEL_PATH.exists():
        model = LSTMForecaster()
        model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu'), weights_only=True))
        model.eval()
        logger.info(f"Model loaded successfully from {MODEL_PATH}")
    else:
        logger.error(f"Model file not found at {MODEL_PATH}")
except Exception as e:
    logger.error(f"Failed to load model: {e}")

@router.post("/make-predictions")
async def make_predictions(request: PredictionRequestModel) -> PredictionResponseModel:
    """
    Make predictions based on the input request.
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Please check server logs.")
    
    # Extract features
    features = [
        request.lat_cell,
        request.lon_cell,
        request.pm25,
        request.mean_no2,
        request.T2M,
        request.T2MDEW,
        request.QV2M,
        request.U10M,
        request.V10M,
        request.PS,
        request.SLP,
        request.TS,
        request.WIND_MAG,
        request.WIND_DIR_DEG,
        request.TEMP_C,
        request.DEWPOINT_C,
        request.n_obs
    ]
    input_tensor = torch.tensor([features], dtype=torch.float32).unsqueeze(0)
    
    with torch.no_grad():
        prediction = model(input_tensor).item()
    
    return PredictionResponseModel(result=np.abs(prediction))
