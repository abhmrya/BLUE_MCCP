
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "it_asset_practice.db"


def get_employees_above_department_average():
    with sqlite3.connect(DB_PATH) as conn:

        query = """
                SELECT name, department, salary
                FROM employees AS e
                WHERE salary > (
                    SELECT AVG(salary)
                    FROM employees
                    WHERE department = e.department
                );
        """

        return conn.execute(query).fetchall()


if __name__ == "__main__":
    for row in get_employees_above_department_average():
        print(row)
