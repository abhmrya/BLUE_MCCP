
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "normalization_practice.db"

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ticket_records (
            ticket_id INTEGER,
            employee_id INTEGER,
            employee_name TEXT,
            department_id INTEGER,
            department_name TEXT,
            issue TEXT
        )
    """)

    count = conn.execute(
        "SELECT COUNT(*) FROM ticket_records"
    ).fetchone()[0]

    if count == 0:
        conn.executemany("""
            INSERT INTO ticket_records VALUES (?, ?, ?, ?, ?, ?)
        """, [
            (101, 1, "Rahul", 10, "IT", "Laptop issue"),
            (102, 1, "Rahul", 10, "IT", "Network issue"),
            (103, 2, "Priya", 10, "IT", "Login issue"),
            (104, 3, "Amit", 20, "HR", "Email issue"),
        ])

    rows = conn.execute("""
        SELECT * FROM ticket_records ORDER BY ticket_id
    """).fetchall()

    for row in rows:
        print(row)

print("Database:", DB_PATH)
