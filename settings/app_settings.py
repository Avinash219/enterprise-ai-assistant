from enum import Enum

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
    CHUNK_SIZE: int
    CHUNK_OVERLAP_SIZE: int
    
    @property
    def is_production(self) -> bool:
        return self.APP_ENV == EnvironmentEnum.PRODUCTION

    
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        extra="ignore"
    )

    
        