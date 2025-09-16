import sqlite3


def crear_base():
    conn = sqlite3.connect('bdd/ventas.db')
    cursor = conn.cursor()

    with open('./bdd/schema.sql', 'r') as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()