
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "it_asset_practice.db"


def get_expensive_assets():
    with sqlite3.connect(DB_PATH) as conn:

        query = """
        select asset_name , purchase_cost
        from assets
        where purchase_cost > (
                select avg(purchase_cost)
                from assets
            )
        order by purchase_cost desc;
        """

        return conn.execute(query).fetchall()


if __name__ == "__main__":
    for row in get_expensive_assets():
        print(row)
