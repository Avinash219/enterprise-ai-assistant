from typing import List

from pydantic import BaseModel


class FileUploadResponse(BaseModel):
    fileName: str
    content: str
    characterCount: int
    chunkData: List[str]