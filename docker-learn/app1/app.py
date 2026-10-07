import os
import redis
import requests
from fastapi import FastAPI

app = FastAPI(title="Docker Learning App 1")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
)


@app.get("/")
def home():
    return {
        "app": "app1",
        "message": "Hello from App 1"
    }


@app.get("/health")
def health():
    return {
        "app": "app1",
        "status": "healthy"
    }


@app.get("/app2")
def call_app2():
    response = requests.get("http://app2:8000/", timeout=5)

    return {
        "app": "app1",
        "app2_response": response.json()
    }


@app.get("/redis")
def redis_test():
    redis_client.set("message", "Hello from Redis")

    value = redis_client.get("message")

    return {
        "redis_value": value
    }