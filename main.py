
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile

from helper.llm_initialize import llm_init
from models.file_upload_response import FileUploadResponse
from models.health_response import HealthResponse
from models.llm_req_res import LLMRequest, LLMResponse
from services.document_chunker import doc_chunk_list
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
    if Path(file.filename).suffix != ".txt":
        raise HTTPException(status_code=400,detail="Only TextFiles are supported")
    if file.size/(1024*1024) > 5:
        raise HTTPException(status_code=400,detail="File size larger than 5 Mb not supported")
    if file.size == 0:
            raise HTTPException(status_code=400,detail="Empty File are not supported")
        
    content = await file.read()
    
    try:
        data = content.decode("utf-8","strict")
        chunkData = doc_chunk_list(data,settings.CHUNK_SIZE,settings.CHUNK_OVERLAP_SIZE)
        return FileUploadResponse(content=data,fileName=file.filename,characterCount = len(data))
    except UnicodeDecodeError:
        raise HTTPException(status_code=400,detail="File must contain valid UTF-8 text")
        
    
