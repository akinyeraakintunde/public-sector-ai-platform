from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = "Public Sector AI Platform (SC-Aligned)"
    environment: str = os.getenv("ENVIRONMENT", "dev")

settings = Settings()
