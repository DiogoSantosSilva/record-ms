from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str
    ENVIRONMENT: str
    DATABASE_URL: str
    HOST: str
    PORT: int

    class Config:
        env_file = ".env"


settings = Settings()
