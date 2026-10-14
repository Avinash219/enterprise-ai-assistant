from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME:str
    
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        extra="ignore"
    )
    
try:
    settings = AppSettings()
except Exception as e:
    print(f"Validation Error {e}")

    
        