from typing import List

from pydantic import BaseModel


class AnswerRequest(BaseModel):
    question: str
    
class AnswerResponse(BaseModel):
    answer: str | None
    sources: List[str]