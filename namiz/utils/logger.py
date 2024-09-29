# namiz/utils/logger.py
import sys
from loguru import logger
from namiz.config import Config

# Remove default logger
logger.remove()

# Configure Loguru
logger.add(
    sys.stdout,
    level=Config.LOG_LEVEL,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    enqueue=True,
    backtrace=True,
    diagnose=True
)

def get_logger(name: str = "namiz"):
    return logger.bind(name=name)
