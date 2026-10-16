from enum import Enum

from pydantic import Field, PositiveInt, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvironmentEnum(str, Enum):
    DEVELOPMENT= "development"
    PRODUCTION= "production"
    
class LLMProvider(str,Enum):
    ANTHROPIC = "Anthropic"
    
class AppSettings(BaseSettings):
    APP_NAME: str
    APP_ENV: EnvironmentEnum
    LLM_MODEL_NAME: str
    LLM_PROVIDER: LLMProvider
    LLM_API_KEY: str
    CHUNK_SIZE: PositiveInt
    CHUNK_OVERLAP_SIZE: int = Field(ge=0)
    
    @property
    def is_production(self) -> bool:
        return self.APP_ENV == EnvironmentEnum.PRODUCTION

    @model_validator(mode='after')
    def compareOverlapSize(self):
        if self.CHUNK_OVERLAP_SIZE >= self.CHUNK_SIZE:
            raise ValueError('Chunk Overlap Size must be less than ChunK Size')
        return self
    
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        extra="ignore"
    )

    
        