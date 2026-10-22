import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "it_asset_practice.db"

if not DB_PATH.is_file():
    raise FileNotFoundError(f"Database not found: {DB_PATH}")

with sqlite3.connect(DB_PATH) as conn:
    tables = conn.execute("""
        SELECT name FROM sqlite_master
        WHERE type = 'table' ORDER BY name;
    """).fetchall()
    print("Database:", DB_PATH)
    print("Tables:", tables)
    for table in ("employees", "technicians", "assets", "tickets"):
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"{table}: {count} rows")
