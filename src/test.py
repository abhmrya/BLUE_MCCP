
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="mylog.log",
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("mylog.log", encoding="utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)


logger.info("Application started")
logger.warning("API response is slow")
logger.error("Failed to save products")

a = 936
b = 936
print(a is b)

c = 9270
d = 9270
logger.info("c and d successfully declared.")
print(c is d)

a = 5
b = 5
print(a == b)

c = 7270
d = 7270
print(c == d)

a = 936
b = 936
print(a is b)

print("test")
print("slash check")
print("same line change")
print("git stash")
print("hello b")
print("hello c")