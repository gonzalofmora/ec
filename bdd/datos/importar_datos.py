from bdd.funciones_db import insertar_datos
from pathlib import Path
import pandas as pd

def importar_datos():

    df = pd.read_csv('bdd/datos/clientes.csv')

    insertar_datos('bdd/ventas.db', df, 'clientes')