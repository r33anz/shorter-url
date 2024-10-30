from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class URLModel(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    url: str
    shortCode: str
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)
    accessCount: int = 0
