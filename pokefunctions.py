"""Functions for interacting with the pokemon database."""

import psycopg2
from psycopg2.extras import RealDictCursor


conn = psycopg2.connect("dbname=pokemon user=dan host=localhost")


def get_all() -> list:
    """Returns a list of all pokemon in the database."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM pokemon;")
        data = cur.fetchall()
        return data


def add_one(data: dict) -> dict:
    """Adds a new pokemon to the database."""
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT COUNT(*) + 1 AS id FROM pokemon;")
    next_id = cur.fetchone()["id"]
    print(next_id)
    cur.execute("""
        INSERT INTO pokemon
            (id, name, height, weight)
        VALUES (%s, %s, %s, %s) RETURNING *;
    """, [next_id, data["name"], data["height"], data["weight"]])
    new_pokemon = cur.fetchone()
    cur.commit()
    cur.close()
    return new_pokemon
