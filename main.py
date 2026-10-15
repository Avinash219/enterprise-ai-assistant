
from fastapi import FastAPI

from helper.llm_initialize import llm_init
from models.health_response import HealthResponse
from models.llm_response import LLMResponse
from settings.app_settings import AppSettings

settings = AppSettings()

model = llm_init(settings.LLM_API_KEY,settings.LLM_MODEL_NAME)

app = FastAPI(
    title=settings.APP_NAME,
    debug=not settings.is_production
)


@app.get("/health")
def health() -> HealthResponse:
    return HealthResponse(message="Ok")


@app.post("/llm-check")
async def llmCheck(query: str):
    result = model.invoke(query)
    return LLMResponse(result=result.content)

