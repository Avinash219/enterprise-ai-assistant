from enum import Enum

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvironmentEnum(str, Enum):
    DEVELOPMENT= "development"
    PRODUCTION= "production"
    
class AppSettings(BaseSettings):
    APP_NAME: str
    APP_ENV: EnvironmentEnum
    
    @computed_field
    @property
    def is_production(self) -> str:
        return self.APP_ENV.value == EnvironmentEnum.PRODUCTION

    
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        extra="ignore"
    )

    
        