import numpy as np
from pydantic import BaseModel, ConfigDict

class ParametersDTO(BaseModel):
    N: int
    G: float
    G_distribution: str
    G_second_parameter: float
    v0_mean: float
    v0_mean_distribution: str
    v0_second_parameter: float
    d_min: float
    d_max: float
    min_angle: float
    max_angle: float
    angle_distribution: str

class DistributionsDTO(BaseModel):
    v0_dist: np.ndarray
    g_dist: np.ndarray
    angles_dist: np.ndarray

    model_config = ConfigDict(arbitrary_types_allowed=True)
