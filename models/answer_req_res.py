from typing import List

from pydantic import BaseModel


class AnswerRequest(BaseModel):
    question: str
    
class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]