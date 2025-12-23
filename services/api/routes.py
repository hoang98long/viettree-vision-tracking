from fastapi import APIRouter
from services.storage.repository import CounterRepository
from services.api.schemas import CountCreate

router = APIRouter()
repo = CounterRepository()

@router.post("/counts")
def create_count(data: CountCreate):
    return repo.create(data)

@router.get("/counts")
def list_counts():
    return repo.list()
