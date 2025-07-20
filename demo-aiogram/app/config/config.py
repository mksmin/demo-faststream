import logging

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseModel):
    token: str


class LoggingConfig(BaseModel):
    level: int = Field(default=logging.INFO)

    @classmethod
    def configurate_logging(cls, level: int = logging.INFO):
        logging.basicConfig(
            level=level,
            datefmt="%Y-%m-%d %H:%M:%S",
            format="[%(asctime)s.%(msecs)03d] %(funcName)20s %(module)10s:%(lineno)5d %(levelname)-8s - %(message)s",
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="BOT_CONFIG__",
    )
    bot: BotConfig
    log: LoggingConfig = Field(default_factory=LoggingConfig)


settings = Settings()
