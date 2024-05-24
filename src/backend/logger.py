from loguru import logger
from config import LOGGER_DIAGNOSE
from sys import stderr


def setup_logger() -> None:
    """Setup the logger for the application."""
    # TODO: Move configuration to config.py
    logger.remove()  # Clear existing sinks

    default_log_format = """<green>{time:YYYY-MM-DD at HH:mm:ss.SSSSZ}</green> | \
<level>{level}</level> | \
<cyan>{file}</cyan>:<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> \
- <level>{message}</level> \
"""

    # Log everything to a file
    logger.add(
        "logs.log",
        serialize=True,
        rotation="500 MB",
        enqueue=True,
        diagnose=LOGGER_DIAGNOSE,
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


# TODO: Move this to lifespan function in endpoints.py after refactoring certificate.py
setup_logger()
