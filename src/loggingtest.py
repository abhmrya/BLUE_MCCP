
import logging

# 1. Create a logger
logger = logging.getLogger("data_pipeline")
logger.setLevel(logging.DEBUG)

# Prevent duplicate propagation to the root logger
logger.propagate = False

# 2. Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 3. Create a file handler
file_handler = logging.FileHandler(
    "pipeline.log",
    encoding="utf-8",
)
file_handler.setLevel(logging.DEBUG)

# 4. Create formatters
console_format = logging.Formatter(
    "%(levelname)s | %(message)s"
)

file_format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# 5. Attach formatters to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# 6. Attach handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 7. Generate log records
logger.debug("Starting API extraction")
logger.info("Extracted 20 products")
logger.warning("API response is slow")
logger.error("Database loading failed")