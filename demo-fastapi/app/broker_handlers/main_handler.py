import asyncio
import logging
from typing import Annotated

from fastapi import Depends, HTTPException
from faststream.rabbit import RabbitBroker, fastapi, RabbitMessage
from pydantic import BaseModel

from app.config import settings

router = fastapi.RabbitRouter(
    settings.rabbit.url,
    prefix="/rabbit",
    tags=["rabbit"],
)
log = logging.getLogger(__name__)


def broker() -> RabbitBroker:
    return router.broker


@router.post("/user")
async def create_user(
    first_name: str,
    last_name: str,
    username: str,
    broker: Annotated[RabbitBroker, Depends(broker)],
):
    log.info(f"Creating user {first_name} {last_name} with username {username}")
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
    }
    try:
        result: RabbitMessage = await broker.request(
            data, queue="input-queue", timeout=3
        )

        return {"result": result.body}
    except asyncio.TimeoutError:
        raise HTTPException(
            status_code=503,
            detail="Service Unavailable",
        )
