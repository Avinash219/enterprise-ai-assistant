
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile

from helper.llm_initialize import llm_init
from models.answer_req_res import AnswerRequest, AnswerResponse
from models.file_upload_response import FileUploadResponse
from models.health_response import HealthResponse
from models.llm_req_res import LLMRequest, LLMResponse
from services.answer_generator import answer_question
from services.vector_store import create_doc_vector
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
        create_doc_vector(file.filename,data,settings.CHUNK_SIZE,settings.CHUNK_OVERLAP_SIZE)
        return FileUploadResponse(content=data,fileName=file.filename,characterCount = len(data))
    except UnicodeDecodeError:
        raise HTTPException(status_code=400,detail="File must contain valid UTF-8 text")

@app.post("/ask",response_model=AnswerResponse)
async def ask(question:AnswerRequest):
    result = await answer_question(model,question.question)
    print(result["res"])
    if isinstance(result["res"], str):
        return AnswerResponse(answer=result["res"],sources = result["citation"])
    return AnswerResponse(answer=result["res"].text,sources = result["citation"])
        
    
