from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.ask import router as ask_router
from app.api.v1.audit import router as audit_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title=settings.app_name)

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(ask_router, prefix="/api/v1", tags=["ask"])
app.include_router(audit_router, prefix="/api/v1", tags=["audit"])

@app.get("/")
def root():
    return {"message": "Public Sector AI Platform API is running"}