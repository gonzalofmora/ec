import sqlite3
import pandas as pd

def importar_schema():     
    conn = sqlite3.connect('bdd/ec.db')
    cursor = conn.cursor()

    with open('./bdd/schema.sql', 'r') as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()

def insertar_datos(db:str, df: pd.DataFrame, tabla:str) -> None:
    with sqlite3.connect(db) as con:
        cols = ",".join(df.columns)
        placeholders = ",".join("?" * len(df.columns))
        sql = f"INSERT OR IGNORE INTO {tabla} ({cols}) VALUES ({placeholders})"
        con.executemany(sql, df.values.tolist())

