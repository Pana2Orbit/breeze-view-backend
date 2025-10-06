from pydantic import BaseModel

class PredictionRequestModel(BaseModel):
    """
    Model for the prediction request
    """
    hour_utc: str = ""
    lat_cell: float
    lon_cell: float
    unit: str = ""
    pm25: float = 0.0
    mean_no2: float = 0.0
    T2M: float = 0.0
    T2MDEW: float = 0.0
    QV2M: float = 0.0
    U10M: float = 0.0
    V10M: float = 0.0
    PS: float = 0.0
    SLP: float = 0.0
    TS: float = 0.0
    WIND_MAG: float = 0.0
    WIND_DIR_DEG: float = 0.0
    TEMP_C: float = 0.0
    DEWPOINT_C: float = 0.0
    valid_flag: bool = True
    n_obs: int = 0
