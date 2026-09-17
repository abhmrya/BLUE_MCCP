from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    print("/ called ...............")
    return {"status": "ok"}