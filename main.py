
from fastapi import FastAPI, UploadFile

from helper.llm_initialize import llm_init
from models.file_upload_response import FileUploadResponse
from models.health_response import HealthResponse
from models.llm_req_res import LLMRequest, LLMResponse
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
async def llmCheck(request: LLMRequest):
    result = await model.ainvoke(request.query)
    return LLMResponse(result=result.content)

@app.post("/documents")
async def uploadDocument(file : UploadFile) -> FileUploadResponse:
    if file.content_type != "text/plain":
        raise Exception("Only TextFiles are supported")
    if file.size/(1024*1024) > 5:
        raise Exception("File size larger than 5 Mb not supported")
    if file.size == 0:
            raise Exception("Empty File are not supported")
        
    content = await file.read()
    print(content)
    
    return FileUploadResponse(content=content,fileName=file.filename)
    
