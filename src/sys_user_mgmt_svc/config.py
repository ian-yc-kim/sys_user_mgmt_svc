from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from sqlalchemy.engine import URL

# Load environment-specific .env file
# Default is `.env.development`, but can be overridden by setting the ENVIRONMENT variable
environment = os.getenv('ENVIRONMENT', 'development')
dotenv_file = f'.env.{environment}'
load_dotenv(dotenv_file)

class Settings(BaseSettings):
    """
    Configuration settings loaded from environment variables.
    """
    ENVIRONMENT: str = environment
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    # Add more configuration settings as needed

    class Config:
        env_file = f".env.{os.getenv('ENVIRONMENT', 'development')}"

settings = Settings()
