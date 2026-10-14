
from fastapi import FastAPI

from models.health_response import HealthResponse
from settings.app_settings import AppSettings

try:
    settings = AppSettings()
except Exception as e:
    print(f"Validation Error {e}")
    raise 


app = FastAPI(
    title= settings.APP_NAME
)

@app.get("/health")
def health() -> HealthResponse:
    return HealthResponse(message="Ok")