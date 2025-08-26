from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loading environments from the .env file"""

    BOT_TOKEN: str

    class Config:
        env_file = "../.env"


# environment variables
settings = Settings()
