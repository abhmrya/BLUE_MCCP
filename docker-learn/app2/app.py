from fastapi import FastAPI

app = FastAPI(title="Docker Learning App 2")


@app.get("/")
def home():
    return {
        "app": "app2",
        "message": "Hello from App 2"
    }


@app.get("/health")
def health():
    return {
        "app": "app2",
        "status": "healthy"
    }