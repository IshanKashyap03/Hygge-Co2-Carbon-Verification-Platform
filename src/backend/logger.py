from loguru import logger
from config import LOGGER_DIR, LOGGER_DIAGNOSE
from sys import stderr

__log_file_switch = True


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
        f"{LOGGER_DIR}logs.log",
        serialize=True,
        rotation=__log_file_retention,
        enqueue=True,
        diagnose=LOGGER_DIAGNOSE,
        format=default_log_format,
        retention="1 week",
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


def __log_file_retention(message, file) -> bool:
    """Switches the log file on a new run"""
    global __log_file_switch
    if __log_file_switch:
        __log_file_switch = False
        return True
    return False
