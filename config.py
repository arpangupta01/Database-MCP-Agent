from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    
    Loads configuration from environment variables.
   
    """
    postgres_host:str=Field(alias="POSTGRES_HOST")
    postgres_port:int=Field(alias="POSTGRES_PORT")
    postgres_db:str=Field(alias="POSTGRES_DB")
    postgres_user:str=Field(alias="POSTGRES_USER")
    postgres_password:str=Field(alias="POSTGRES_PASSWORD")
    llm_key:str=Field(alias="OPENAI_API_KEY")
    
    model_config=SettingsConfigDict(
        env_file=".env",
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
    
    