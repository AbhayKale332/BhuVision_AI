from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # .env file path
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()