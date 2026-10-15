
from fastapi import FastAPI

from helper.llm_initialize import llm_init
from models.health_response import HealthResponse
from settings.app_settings import AppSettings

settings = AppSettings()

client = llm_init(settings.LLM_API_KEY)

app = FastAPI(
    title=settings.APP_NAME,
    debug=not settings.is_production
)


@app.get("/health")
def health() -> HealthResponse:
    return HealthResponse(message="Ok")


@app.get("/llm-check")
async def llmCheck(query: str):
    result = await client.messages.create(
     max_tokens=1024,
     messages=[
         {
             "role": "user",
             "content": query
         }
     ]  ,
     model=settings.LLM_MODEL_NAME 
    )
    return {
        "result" : result.content[0].text
    }

