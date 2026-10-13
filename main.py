
from fastapi import FastAPI

from models.health_response import HealthResponse

app = FastAPI()

@app.get("/health")
def health() -> HealthResponse:
    return {
        "message" : "Ok"
    }
    