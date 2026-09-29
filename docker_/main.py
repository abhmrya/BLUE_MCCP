from fastapi import FastAPI
import os
import json

import psycopg
import redis

app = FastAPI(title="FastAPI + PostgreSQL + Redis")


# --------------------------------------------------
# Environment variables
# --------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")


# --------------------------------------------------
# PostgreSQL connection
# --------------------------------------------------

def get_db_connection():
    return psycopg.connect(DATABASE_URL)


# --------------------------------------------------
# Redis connection
# --------------------------------------------------

def get_redis_connection():
    return redis.from_url(
        REDIS_URL,
        decode_responses=True
    )


# --------------------------------------------------
# Home
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI + PostgreSQL + Redis",
        "database": "PostgreSQL",
        "cache": "Redis"
    }


# --------------------------------------------------
# PostgreSQL health check
# --------------------------------------------------

@app.get("/postgres")
def postgres_test():

    try:
        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT version();")

        version = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return {
            "status": "connected",
            "database": "PostgreSQL",
            "version": version
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# Create users table
# --------------------------------------------------

@app.post("/users/create-table")
def create_users_table():

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL
            );
            """
        )

        conn.commit()

        cursor.close()
        conn.close()

        return {
            "message": "users table created successfully"
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# Insert user
# --------------------------------------------------

@app.post("/users/{name}/{age}")
def create_user(name: str, age: int):

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (name, age)
            VALUES (%s, %s)
            RETURNING id, name, age;
            """,
            (name, age)
        )

        user = cursor.fetchone()

        conn.commit()

        cursor.close()
        conn.close()

        return {
            "message": "User created",
            "user": {
                "id": user[0],
                "name": user[1],
                "age": user[2]
            }
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# Get users
# --------------------------------------------------

@app.get("/users")
def get_users():

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, name, age
            FROM users
            ORDER BY id;
            """
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        users = []

        for row in rows:

            users.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "age": row[2]
                }
            )

        return {
            "users": users
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# Redis health check
# --------------------------------------------------

@app.get("/redis")
def redis_test():

    try:

        r = get_redis_connection()

        response = r.ping()

        return {
            "status": "connected",
            "redis": response
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# Redis set value
# --------------------------------------------------

@app.post("/cache/{key}/{value}")
def set_cache(key: str, value: str):

    try:

        r = get_redis_connection()

        r.set(key, value)

        return {
            "message": "Value stored in Redis",
            "key": key,
            "value": value
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# Redis get value
# --------------------------------------------------

@app.get("/cache/{key}")
def get_cache(key: str):

    try:

        r = get_redis_connection()

        value = r.get(key)

        if value is None:

            return {
                "message": "Key not found",
                "key": key
            }

        return {
            "key": key,
            "value": value
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }