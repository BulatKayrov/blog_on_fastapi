from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    PROD_DEV: bool

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ACCESS_TOKEN_COOKIE_NAME: str = "token"

    @property
    def database_url(self) -> str:
        """
        Return the database url if we are in prod or dev
        :return: URL
        """
        if self.PROD_DEV:
            return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}"
        return "sqlite+aiosqlite:///db.sqlite3"


settings = Settings()
