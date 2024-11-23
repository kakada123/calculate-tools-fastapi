from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Tool API"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
