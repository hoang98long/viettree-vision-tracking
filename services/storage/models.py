from sqlalchemy import Column, Integer, String, DateTime
from services.storage.database import Base

class Count(Base):
    __tablename__ = "counts"

    id = Column(Integer, primary_key=True)
    device_id = Column(String)
    class_name = Column(String)
    value = Column(Integer)
    timestamp = Column(DateTime)
