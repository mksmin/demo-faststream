import logging

from faststream import Logger
from faststream.rabbit import RabbitBroker
from typing import Any

from app.config import settings

broker = RabbitBroker(settings.rabbit.url)
log = logging.getLogger(__name__)


@broker.subscriber("input-queue")
async def test_handler(msg: dict[str, Any]):
    log.info(f"Get message: %s", msg)

    processed_msg = (f"{k.upper()}={v.upper()}" for k, v in msg.items())
    return ", ".join(processed_msg)
