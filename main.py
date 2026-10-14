
from fastapi import FastAPI

from models.health_response import HealthResponse
from settings.app_settings import AppSettings

settings = AppSettings()
DEBUG_MODE = False

app = FastAPI(
    title=settings.APP_NAME
)

if not settings.is_production:
    DEBUG_MODE = True

@app.get("/health")
def health() -> HealthResponse:
    return HealthResponse(message="Ok")