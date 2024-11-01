from pydantic import BaseModel
from datetime import datetime

class UlrResponseDTO(BaseModel):
    url : str
    shortCode: str
    createdAt: datetime
    updatedAt: datetime

class UrlCreateDTO(BaseModel):
    url : str

class UlrResponseStatsDTO(BaseModel):
    url : str
    shortCode: str
    accessCount: int
    createdAt: datetime
    updatedAt: datetime