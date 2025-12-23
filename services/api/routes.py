from fastapi import APIRouter
from services.api.schemas import EdgePayload
from services.storage.repository import CounterRepository

router = APIRouter()
repo = CounterRepository()

@router.post("/edge/push")
def push_from_edge(payload: EdgePayload):
    repo.save_payload(payload)
    return {"status": "ok"}
