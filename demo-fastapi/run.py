import logging
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel

from app.config import settings
from app.api import api_router
from app.broker_handlers.main_handler import router as broker_router

settings.log.configurate_logging()
log = logging.getLogger(__name__)


class Runner(BaseModel):
    app: str = "run:app"
    host: str = settings.run.host
    port: int = settings.run.port
    log_level: str = settings.run.log_level
    reload: bool = settings.run.reload


run_config = Runner()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Starting FastAPI server")
    yield
    log.info("Stopping FastAPI server")


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    api_router,
)
app.include_router(
    broker_router,
)


if __name__ == "__main__":
    try:
        uvicorn.run(**run_config.model_dump(exclude_none=True)),
    except KeyboardInterrupt:
        log.warning("Bye!")
