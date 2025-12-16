from fastapi import FastAPI
from backend.app.api.v1.health import router as health_router
from backend.app.core.config import settings
from backend.app.core.logging import setup_logging

setup_logging()

app = FastAPI(title=settings.app_name)

app.include_router(health_router, prefix="/api/v1", tags=["health"])

@app.get("/")
def root():
    return {"message": "Public Sector AI Platform API is running"}
from backend.app.api.v1.ask import router as ask_router