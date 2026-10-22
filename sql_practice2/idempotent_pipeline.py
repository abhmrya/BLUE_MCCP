
import csv
import logging
import sqlite3
from pathlib import Path

# ---------- Configuration ----------

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "pipeline_practice.db"
CSV_PATH = BASE_DIR / "daily_tickets.csv"

REQUIRED_COLUMNS = {
    "ticket_id",
    "category",
    "status",
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


# ---------- Step 1: Create sample input ----------

def create_sample_csv():
    """Create sample input only when the file does not exist."""

    if CSV_PATH.exists():
        logging.info("Input CSV already exists; keeping existing data.")
        return

    rows = [
        ["T001", "hardware", "open"],
        ["T002", "network", "closed"],
        ["T003", "software", "open"],
        ["T002", "network", "closed"],  # Duplicate in the same file
        ["T004", "security", "in_progress"],
    ]

    with CSV_PATH.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["ticket_id", "category", "status"])
        writer.writerows(rows)

    logging.info("Sample CSV created: %s", CSV_PATH.name)


# ---------- Step 2: Create database ----------

def create_database():
    """Create a table with a unique ticket identifier."""

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                status TEXT NOT NULL,
                loaded_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

    logging.info("Database and table are ready.")


# ---------- Step 3: Validate input ----------

def validate_ticket(row):
    """Validate a single CSV record."""

    ticket_id = (row.get("ticket_id") or "").strip()
    category = (row.get("category") or "").strip().lower()
    status = (row.get("status") or "").strip().lower()

    allowed_statuses = {"open", "closed", "in_progress"}

    if not ticket_id:
        raise ValueError("ticket_id is missing")

    if not category:
        raise ValueError("category is missing")

    if status not in allowed_statuses:
        raise ValueError(f"Invalid status: {status!r}")

    return ticket_id, category, status


# ---------- Step 4: Load data safely ----------

def load_tickets():
    """Load tickets without inserting duplicate ticket IDs."""

    if not CSV_PATH.is_file():
        raise FileNotFoundError(f"Input file not found: {CSV_PATH}")

    rows_read = 0
    inserted = 0
    duplicates = 0
    rejected = 0

    with CSV_PATH.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV is empty or has no header.")

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                f"Missing CSV columns: {sorted(missing_columns)}"
            )

        # The transaction commits only after processing completes.
        with sqlite3.connect(DB_PATH) as connection:

            for line_number, row in enumerate(reader, start=2):
                rows_read += 1

                try:
                    ticket = validate_ticket(row)

                except ValueError as error:
                    rejected += 1
                    logging.warning(
                        "Rejected CSV line %s: %s",
                        line_number,
                        error,
                    )
                    continue

                cursor = connection.execute("""
                    INSERT INTO tickets
                        (ticket_id, category, status)
                    VALUES (?, ?, ?)
                    ON CONFLICT(ticket_id) DO NOTHING
                """, ticket)

                if cursor.rowcount == 1:
                    inserted += 1
                else:
                    duplicates += 1

    logging.info(
        "Pipeline summary | read=%s | inserted=%s | "
        "duplicates=%s | rejected=%s",
        rows_read,
        inserted,
        duplicates,
        rejected,
    )

    return {
        "read": rows_read,
        "inserted": inserted,
        "duplicates": duplicates,
        "rejected": rejected,
    }


# ---------- Step 5: Verify the results ----------

def show_tickets():
    """Display the final tickets stored in the database."""

    with sqlite3.connect(DB_PATH) as connection:
        rows = connection.execute("""
            SELECT ticket_id, category, status
            FROM tickets
            ORDER BY ticket_id
        """).fetchall()

    print("\n========== DATABASE RECORDS ==========")

    for ticket in rows:
        print(ticket)

    print(f"\nTotal unique tickets: {len(rows)}")


# ---------- Step 6: Run the pipeline ----------

def main():
    """Execute the pipeline."""

    try:
        create_sample_csv()
        create_database()
        load_tickets()
        show_tickets()

    except (sqlite3.Error, OSError, ValueError) as error:
        logging.error("Pipeline failed: %s", error)
        raise


if __name__ == "__main__":
    main()
