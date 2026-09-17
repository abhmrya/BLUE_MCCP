import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)


file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)


logger.debug("Debug message")
logger.info("Application started")
logger.warning("Something unusual happened")
logger.error("Something failed")
