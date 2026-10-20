import sqlite3

from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "assetops.db"

connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()

print("connected successfully!.")

# tables = cursor.execute("select * from employees").fetchall()

# print(tables)

tables = cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""").fetchall()

print("Table:", tables)

connection.close()