
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "indexing_practice.db"


def setup_database():
    """Create a separate database with sample ticket data."""

    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id INTEGER PRIMARY KEY,
                ticket_code TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL,
                created_by TEXT NOT NULL
            )
        """)

        count = connection.execute(
            "SELECT COUNT(*) FROM tickets"
        ).fetchone()[0]

        if count == 0:
            categories = [
                "hardware", "network", "software", "security"
            ]
            statuses = ["open", "closed", "in_progress"]
            users = ["Abhay", "Priya", "Rahul", "Neha"]

            tickets = [
                (
                    i,
                    f"TCK-{i:05d}",
                    categories[i % len(categories)],
                    statuses[i % len(statuses)],
                    users[i % len(users)]
                )
                for i in range(1, 10001)
            ]

            connection.executemany("""
                INSERT INTO tickets
                (ticket_id, ticket_code, category, status, created_by)
                VALUES (?, ?, ?, ?, ?)
            """, tickets)

        # Reset the practice index so every run starts fairly.
        connection.execute("""
            DROP INDEX IF EXISTS idx_tickets_ticket_code
        """)

        connection.commit()
        print("Practice database is ready.")

    finally:
        connection.close()


def optimize_ticket_search():
    """Compare query plans before and after indexing."""

    connection = None

    try:
        connection = sqlite3.connect(DB_PATH)

        # TODO 1: Inspect the query plan BEFORE creating an index.
        # Search for ticket_code = 'TCK-09999'.
        # Use EXPLAIN QUERY PLAN.

        query_plan = """
            SELECT *
            FROM tickets
            WHERE ticket_code = 'TCK-09999';
        """

        result = connection.execute(query_plan).fetchall()

        print("\nBEFORE INDEX")
        for row in result:
            print(row)

        # TODO 2: Create an index named
        # idx_tickets_ticket_code on ticket_code.
        connection.execute("""
                    create index if not exists idx_tickets_ticket_code
                    on tickets(ticket_code)
                            """)

        # TODO 3: Run EXPLAIN QUERY PLAN again
        # using the same search query.

        result = connection.execute(query_plan).fetchall()

        print("\n ============ AFTER INDEX ==============")

        for row in result:
            print(row)

        # TODO 4: Print the result under AFTER INDEX.

        search_query = """
                select *
                from tickets
                where ticket_code = ?
            """

        ticket = connection.execute(
            search_query, ("TCK-09999")
        ).fetchone()

        # TODO 5: Execute the actual search and print
        # the matching ticket.
        print("\n========== FOUND TICKET ==========")
        print(ticket)

    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    setup_database()
    optimize_ticket_search()
