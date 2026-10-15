from pydantic import BaseModel


class LLMResponse(BaseModel):
    result: str
    
class LLMRequest(BaseModel):
    query: str