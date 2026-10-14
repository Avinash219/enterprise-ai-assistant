from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvironmentEnum(str, Enum):
    DEVELOPMENT= "development"
    PRODUCTION= "production"
    
class AppSettings(BaseSettings):
    APP_NAME: str
    APP_ENV: EnvironmentEnum
    
    @property
    def is_production(self) -> bool:
        return self.APP_ENV == EnvironmentEnum.PRODUCTION

    
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        extra="ignore"
    )

    
        