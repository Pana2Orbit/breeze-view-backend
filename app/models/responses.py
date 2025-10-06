from pydantic import BaseModel

class PredictionResponseModel(BaseModel):
    """
    Model for the prediction response
    """
    result: float