import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")


file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=1024,
    backupCount=3,
)

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


for i in range(1000):
    logger.info(
        "This is a test log message number %s",
        i,
    )
