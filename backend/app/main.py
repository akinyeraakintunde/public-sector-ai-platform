

from app.api.v1.health import router as health_router
from app.api.v1.ask import router as ask_router
from app.api.v1.audit import router as audit_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

from fastapi import FastAPI

app = FastAPI(
    title="Public Sector AI Platform (Demo)",
    description="Multi-agent AI platform for public-sector decision intelligence",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}