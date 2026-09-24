from fastapi import FastAPI


import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
environment = os.getenv("APP_ENV")
api_key = os.getenv("API_KEY")

print("App:", app_name)
print("Environment:", environment)
print("API Key:", api_key)

app = FastAPI()


@app.get("/")
def home():
    API_KEY = os.getenv("API_KEY")
    print(API_KEY)
    return {"message": "Hello from Docker + FastAPI"}


@app.get("/users")
def users():
    return {"users": ["Abhay", "Amit", "Suresh"]}