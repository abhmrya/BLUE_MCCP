from fastapi import FastAPI
import os
import redis

app = FastAPI()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)


@app.get("/")
def root():
    visits = redis_client.incr("visits")

    return {
        "message": "Hello from FastAPI + Docker Compose",
        "visits": visits
    }