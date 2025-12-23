from services.storage.database import SessionLocal
from services.storage.models import Count

class CounterRepository:
    def create(self, data):
        db = SessionLocal()
        obj = Count(**data.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        db.close()
        return obj

    def list(self):
        db = SessionLocal()
        res = db.query(Count).all()
        db.close()
        return res
