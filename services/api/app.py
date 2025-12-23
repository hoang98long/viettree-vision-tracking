from fastapi import FastAPI
from services.storage.database import engine, Base
from services.api.routes import router

app = FastAPI(title="VietTree Vision API")

Base.metadata.create_all(bind=engine)
app.include_router(router)
