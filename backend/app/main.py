from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.api.v1.ask import router as ask_router
from app.api.v1.audit import router as audit_router
from app.core.config import settings
from app.core.logging import setup_logging