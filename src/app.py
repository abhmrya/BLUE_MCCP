
import logging

from logger_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def process_data() -> list[int]:
    logger.info("Starting data processing")

    data = [10, 20, 30]
    logger.info("Loaded %d records", len(data))

    result = [value * 2 for value in data]
    logger.info("Data processing completed")

    return result


if __name__ == "__main__":
    process_data()