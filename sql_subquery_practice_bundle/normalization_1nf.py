
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "normalization_practice.db"

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bad_tickets (
            ticket_id INTEGER PRIMARY KEY,
            employee_name TEXT NOT NULL,
            issues TEXT NOT NULL
        )
    """)

    count = conn.execute(
        "SELECT COUNT(*) FROM bad_tickets"
    ).fetchone()[0]

    if count == 0:
        conn.executemany(
            "INSERT INTO bad_tickets VALUES (?, ?, ?)",
            [
                (101, "Rahul", "Laptop, Network"),
                (102, "Priya", "Login"),
                (103, "Amit", "Email, Printer, Wi-Fi"),
            ],
        )

    rows = conn.execute(
        "SELECT * FROM bad_tickets ORDER BY ticket_id"
    ).fetchall()

    for row in rows:
        print(row)
