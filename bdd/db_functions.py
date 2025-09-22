import sqlite3
import pandas as pd

def crear_base():     
    conn = sqlite3.connect('bdd/ventas.db')
    cursor = conn.cursor()

    with open('./bdd/schema.sql', 'r') as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()

def insertar_datos(db:str, df: pd.DataFrame) -> None:
    with sqlite3.connect(db) as con:
        cur = con.cursor()
        cols = ",".join(df.columns)
        placeholders = ",".join("?" * len(df.columns))
        sql = f"INSERT OR IGNORE INTO ventas ({cols}) VALUES ({placeholders})"
        con.executemany(sql, df.values.tolist())
