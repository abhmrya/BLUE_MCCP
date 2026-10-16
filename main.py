
# import logging
# import time

# from src.logger_config import setup_logging

# setup_logging()
# logger = logging.getLogger(__name__)


# def extract_products() -> list[dict]:
#     logger.info(
#         "Starting product extraction",
#         extra={
#             "event": "extraction_started",
#             "pipeline": "fake_store",
#         },
#     )

#     products = [
#         {"id": 1, "title": "Laptop"},
#         {"id": 2, "title": "Phone"},
#     ]

#     logger.info(
#         "Products extracted",
#         extra={
#             "event": "products_extracted",
#             "count": len(products),
#             "pipeline": "fake_store",
#         },
#     )

#     return products


# def transform_products(products: list[dict]) -> list[dict]:
#     start = time.perf_counter()

#     transformed = [
#         {
#             "product_id": product["id"],
#             "product_name": product["title"],
#         }
#         for product in products
#     ]

#     duration_ms = round(
#         (time.perf_counter() - start) * 1000, 2
#     )

#     logger.info(
#         "Products transformed",
#         extra={
#             "event": "transformation_completed",
#             "count": len(transformed),
#             "duration_ms": duration_ms,
#         },
#     )

#     return transformed


# def run_pipeline() -> None:
#     logger.info(
#         "Pipeline started",
#         extra={"event": "pipeline_started"},
#     )

#     try:
#         products = extract_products()
#         transformed = transform_products(products)

#         logger.info(
#             "Pipeline completed",
#             extra={
#                 "event": "pipeline_completed",
#                 "output_count": len(transformed),
#             },
#         )

#     except Exception:
#         logger.exception(
#             "Pipeline failed",
#             extra={"event": "pipeline_failed"},
#         )
#         raise


# if __name__ == "__main__":
#     run_pipeline()




import logging
import structlog

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler()],
)

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

logger.info("application_started")
logger.warning("api_response_slow", endpoint="/products")
logger.error("database_load_failed", database="postgres")