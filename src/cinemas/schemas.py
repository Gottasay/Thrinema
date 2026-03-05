from fastapi import BaseModel, Query
from typing import Optional
from datetime import date

class Cinema(BaseModel):
    id: int
    country: str
    location: str
    name: str
    rating: Optional[float] = Query(None, ge=1.0, le=5.0)
    created_at: date