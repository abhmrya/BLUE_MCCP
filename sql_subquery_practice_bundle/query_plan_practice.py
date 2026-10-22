
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "it_asset_practice.db"

with sqlite3.connect(DB_PATH) as conn:\

    conn.execute("""
        create index if not exists idx_tickets_status
        on tickets(status);            
""")
    
    

    query = """
    SELECT *
    FROM tickets
    WHERE status = 'open';
    """

    plan = conn.execute(
        "EXPLAIN QUERY PLAN " + query
    ).fetchall()

    for row in plan:
        print(row)
