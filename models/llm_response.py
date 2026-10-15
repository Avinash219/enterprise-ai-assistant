from pydantic import BaseModel


class LLMResponse(BaseModel):
    result: str