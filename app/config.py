from pydantic_settings import BaseSettings
# from pydantic import root_validator


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    SEKRET_KEY: str
    ALGORITM_JWT: str

    class Config:
        env_file = '.env'

settings = Settings()
