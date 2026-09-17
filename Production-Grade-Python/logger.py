import logging

# logging.basicConfig(
#     level=logging.DEBUG,
# )

# logger = logging.getLogger(__name__)


# logging.info("Application started")

# logging.warning("Something looks wrong")
# logging.error("Something failed")

# logger = logging.getLogger(__name__)

# logger.info("Application started")
# logger.warning("Something unusual happened")
# logger.error("Something failed")


# def divide(a: int, b: int) -> float:
#     logger.debug("Starting division")

#     if b == 0:
#         logger.error("Division by zero attempted")
#         raise ZeroDivisionError("Cannot divide by zero")

#     return a / b

# # divide(10, 0)

# try:
#     result = divide(10, 0)

# except ZeroDivisionError:
#     pass
#     # logger.exception("Division failed")
# except Exception:
#     print("can not divied by 0")


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(name)s:%(message)s",
)

logger = logging.getLogger(__name__)


def divide(a: int, b: int) -> float:
    logger.debug("Starting division")

    if b == 0:
        logger.error("Division by zero attempted")
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


try:
    result = divide(10, 0)

except ZeroDivisionError:
    logger.exception("Division failed")

except Exception:
    logger.exception("Unexpected error")
