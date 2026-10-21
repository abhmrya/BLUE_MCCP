import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "assetops.db"


# def get_tickets():
#     """Fetch the first 10 tickets from the database."""

#     try:
#         connection = sqlite3.connect(DB_PATH)

#         rows = connection.execute("""
#             SELECT *
#             FROM tickets
#             LIMIT 10
#         """).fetchall()

#         print(rows)
#         connection.close()

#     except sqlite3.Error as error:
#         print(f"Database error: {error}")


# # get_tickets()


# def count_open_tickets():
#     """Count and display the number of open tickets."""

#     try:
#         connection = sqlite3.connect(DB_PATH)

#         result = connection.execute("""
#             SELECT COUNT(*)
#             FROM tickets
#             WHERE closed_on IS NULL
#         """).fetchone()

#         print("*********************************")
#         print("Total open tickets:", result[0])

#         connection.close()

#     except sqlite3.Error as error:
#         print(f"Database error: {error}")


# count_open_tickets()




# def count_closed_tickets():
#     """Count and display the number of closed tickets."""

#     try:
#         connection = sqlite3.connect(DB_PATH)

#         # TODO 1: Count tickets that have been closed.
#         query = """
#             SELECT COUNT(*)
#             FROM tickets
#             WHERE closed_at IS NOT NULL
#         """

#         # TODO 2 and 3: Execute the query and fetch one result.
#         result = connection.execute(query).fetchone()

#         # TODO 4: Print a separator.
#         print("*********************************")

#         # TODO 5: Display the count.
#         print("Total closed tickets:", result[0])

#         # TODO 6: Close the connection.
#         connection.close()

#     except sqlite3.Error as error:
#         print(f"Database error: {error}")

# count_closed_tickets()


# def rank_ticket_categories():
#     """Rank ticket categories based on their total ticket count."""

#     try:
#         connection = sqlite3.connect(DB_PATH)

#         query = """
#             WITH category_counts AS (
#                 SELECT category, COUNT(*) AS total_tickets
#                 FROM tickets
#                 GROUP BY category
#             )
#             SELECT
#                 RANK() OVER (
#                     ORDER BY total_tickets DESC
#                 ) AS category_rank,
#                 category,
#                 total_tickets
#             FROM category_counts
#             ORDER BY category_rank;
#         """

#         result = connection.execute(query).fetchall()

#         print("*********************************")

#         for row in result:
#             print(
#                 f"Rank: {row[0]} | "
#                 f"Category: {row[1]} | "
#                 f"Tickets: {row[2]}"
#             )

#         connection.close()

#     except sqlite3.Error as error:
#         print(f"Database error: {error}")


# rank_ticket_categories()

# import sqlite3
# from pathlib import Path

# DB_PATH = Path(__file__).resolve().parent / "assetops.db"


# def category_ticket_running_total():
#     """Display ticket counts and running totals by category."""

#     connection = None

#     try:
#         connection = sqlite3.connect(DB_PATH)

#         query = """
#             WITH category_counts AS (
#                 SELECT
#                     category,
#                     COUNT(*) AS total_tickets
#                 FROM tickets
#                 GROUP BY category
#             )
#             SELECT
#                 category,
#                 total_tickets,
#                 SUM(total_tickets) OVER (
#                     ORDER BY category
#                     ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
#                 ) AS running_total
#             FROM category_counts
#             ORDER BY category;
#         """

#         # Execute the query and fetch all rows.
#         result = connection.execute(query).fetchall()

#         print("*********************************")
#         print("Ticket Category Running Total")
#         print("*********************************")

#         # Display the results.
#         for row in result:
#             print(
#                 f"Category: {row[0]} | "
#                 f"Tickets: {row[1]} | "
#                 f"Running Total: {row[2]}"
#             )

#     except sqlite3.Error as error:
#         print(f"Database error: {error}")

#     finally:
#         if connection is not None:
#             connection.close()


# category_ticket_running_total()





def technician_leaderboard():
    """Rank technicians by the number of tickets they handled."""

    try:
        connection = sqlite3.connect(DB_PATH)

        query = """
            WITH technician_counts AS (
                SELECT
                    technician,
                    COUNT(*) AS total_tickets
                FROM tickets
                GROUP BY technician
            )
            SELECT
                RANK() OVER (
                    ORDER BY total_tickets DESC
                ) AS technician_rank,
                technician,
                total_tickets
            FROM technician_counts
            ORDER BY technician_rank
            LIMIT 3;
        """

        result = connection.execute(query).fetchall()

        print("***********************")

        for row in result:
            print(
                f"Rank: {row[0]} | "
                f"Technician: {row[1]} | "
                f"Total Tickets: {row[2]}"
            )

        connection.close()

    except sqlite3.Error as error:
        print(f"Database error: {error}")


technician_leaderboard()
