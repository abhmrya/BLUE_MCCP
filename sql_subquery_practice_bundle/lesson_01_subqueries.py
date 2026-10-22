import sqlite3
from pathlib import Path

# Always look for the database beside this Python file.
DB_PATH = Path(__file__).resolve().parent / "it_asset_practice.db"


def get_employees_below_average_salary():
    """Return employees earning below the company-wide average."""

    if not DB_PATH.is_file():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}. Keep the DB beside this script."
        )

    with sqlite3.connect(DB_PATH) as conn:
        # TODO 1:
        # Select employee name and salary from employees.

        # TODO 2:
        # Use a nested query to calculate AVG(salary) across ALL employees.
        # Keep employees whose salary is less than that average.

        # TODO 3:
        # Sort results by salary from lowest to highest.

        query = """
            select name , salary
            from employees
            where salary < (
                    select avg(salary)
                    from employees
                )
            order by salary asc;
        """

        cursor = conn.execute(query)
        return cursor.fetchall()


if __name__ == "__main__":
    print("Database:", DB_PATH)
    with sqlite3.connect(DB_PATH) as conn:
        tables = conn.execute("""
            SELECT name FROM sqlite_master
            WHERE type = 'table' ORDER BY name;
        """).fetchall()
        print("Tables:", tables)

    print("\nEmployees earning below average salary:")
    for row in get_employees_below_average_salary():
        print(row)
