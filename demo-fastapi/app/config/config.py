import logging

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingConfig(BaseSettings):
    level: int = Field(default=logging.INFO)

    @classmethod
    def configurate_logging(cls, level: int = logging.INFO):
        logging.basicConfig(
            level=level,
            datefmt="%Y-%m-%d %H:%M:%S",
            format="[%(asctime)s.%(msecs)03d] %(funcName)20s %(module)10s:%(lineno)5d %(levelname)-8s - %(message)s",
        )


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "info"
    reload: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../../../demo-aiogram/.env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="API_CONFIG__",
    )

    log: LoggingConfig = Field(default_factory=LoggingConfig)
    run: RunConfig = Field(default_factory=RunConfig)


settings = Settings()
