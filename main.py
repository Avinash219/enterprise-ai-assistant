
from fastapi import FastAPI

from models.health_response import HealthResponse
from settings.app_settings import AppSettings

app = FastAPI()

try:
    settings = AppSettings()
except Exception as e:
    print(f"Validation Error {e}")
    raise 

@app.get("/health")
def health() -> HealthResponse:
    return HealthResponse(message="Ok")