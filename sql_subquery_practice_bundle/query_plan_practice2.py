
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "it_asset_practice.db"

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_tickets_status_date
        ON tickets(status, created_date);
    """)

    query = """
        SELECT ticket_id, status, created_date
        FROM tickets
        WHERE status = 'open'
          AND created_date >= '2026-01-10'
        ORDER BY created_date;
    """

    plan = conn.execute(
        "EXPLAIN QUERY PLAN " + query
    ).fetchall()

    print("Query plan:")
    for row in plan:
        print(row)

    print("\nResults:")
    for row in conn.execute(query):
        print(row)


with sqlite3.connect(DB_PATH) as conn:
    indexes = conn.execute("""
        SELECT name, tbl_name, sql
        FROM sqlite_master
        WHERE type = 'index'
          AND tbl_name = 'tickets'
        ORDER BY name;
    """).fetchall()

    for index in indexes:
        print(index)
