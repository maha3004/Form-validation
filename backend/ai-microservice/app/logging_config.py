from loguru import logger
from .config import get_settings


def configure_logging():
    settings = get_settings()
    logger.remove()
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=settings.log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    )


configure_logging()
