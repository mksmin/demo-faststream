import logging

from pydantic import BaseModel, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote


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


class RabbitConfig(BaseModel):
    host: str = "localhost"
    port: int = 5672
    username: str = "guest"
    password: str = "guest"
    vhostname: str | None = None

    @computed_field
    @property
    def url(self) -> str:
        safe_username = quote(self.username, safe="")
        safe_password = quote(self.password, safe="")
        if self.vhostname:
            safe_vhostname = quote(self.vhostname, safe="")

        return f"amqp://{safe_username}:{safe_password}@{self.host}:{self.port}/{safe_vhostname if self.vhostname else ''}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="BOT_CONFIG__",
    )
    bot: BotConfig
    log: LoggingConfig = Field(default_factory=LoggingConfig)
    rabbit: RabbitConfig = Field(default_factory=RabbitConfig)


settings = Settings()
