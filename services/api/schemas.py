from pydantic import BaseModel
from datetime import datetime

class CountCreate(BaseModel):
    device_id: str
    class_name: str
    value: int
    timestamp: datetime
