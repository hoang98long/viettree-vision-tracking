from services.storage.database import SessionLocal
from services.storage.models import Count

class CounterRepository:
    def save_payload(self, payload):
        db = SessionLocal()
        for cls, val in payload.counts.items():
            obj = Count(
                device_id=payload.device_id,
                class_name=cls,
                value=val,
                timestamp=payload.timestamp
            )
            db.add(obj)
        db.commit()
        db.close()
