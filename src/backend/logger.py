from loguru import logger
from config import LOGGER_DIAGNOSE
from sys import stderr


def logger_setup() -> None:
    """Setup the logger for the application."""
    # TODO: Move configuration to config.py
    logger.remove()  # Clear existing sinks

    default_log_format = """<green>{time:YYYY-MM-DD at HH:mm:ss.SSSSZ}</green> | \
<level>{level: <8}</level> | \
<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> \
- <level>{message}</level> \
"""

    # Log everything to a file
    logger.add(
        "logs.log",
        serialize=True,
        rotation="500 MB",
        enqueue=True,
        diagnose=LOGGER_DIAGNOSE,
        format=default_log_format,
    )

    # Log warnings and above to stderr
    logger.add(
        stderr,
        diagnose=LOGGER_DIAGNOSE,
        format=default_log_format,
        level="WARNING",
        colorize=True,
        enqueue=True,
    )


async def logger_close() -> None:
    """Close the logger for the application."""
    await logger.complete()
    logger.remove()  # Clear existing sinks to prevent semaphore leakage


# TODO: Move this to lifespan function in endpoints.py after refactoring certificate.py
logger_setup()
