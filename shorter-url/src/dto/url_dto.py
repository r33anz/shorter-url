from pydantic import BaseModel

class UlrResponseDTO(BaseModel):
    url : str
    shortCode: str
    accessCount: int

class UrlCreateFTO(BaseModel):
    url : str


