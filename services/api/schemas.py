from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class EdgePayload(BaseModel):
    device_id: str
    timestamp: datetime
    counts: Dict[str, int]
