from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str | None = None

    model_config = SettingsConfigDict(env_file='.env')

    @model_validator(mode='after')
    def assemble_db_url(self) -> 'Settings':
        if not self.DATABASE_URL:
            self.DATABASE_URL = (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
        return self


settings = Settings()
print(settings.DATABASE_URL)