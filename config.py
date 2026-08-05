from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

PROJECT_ROOT = Path(__file__).resolve().parent

class Settings(BaseSettings):
    """
    
    Loads configuration from environment variables.
   
    """
    postgres_host: str = Field(alias="POSTGRES_HOST")
    postgres_port: int = Field(alias="POSTGRES_PORT")
    postgres_db: str = Field(alias="POSTGRES_DB")
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD")
    llm_key: str = Field(alias="OPENAI_API_KEY")

    model_config = SettingsConfigDict(
        env_file=str(PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )
    
    @property
    def database_url(self)->str:
        """
        Constructs the database URL from the provided settings.
        
        Returns:
            str: The constructed database URL.
        """
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
@lru_cache
def get_settings() -> Settings:
    """
    Retrieves the settings instance, utilizing caching for efficiency.

    Returns:
        Settings: The settings instance.
    """
    return Settings()
    
    