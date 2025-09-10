# afip_mis_comprobantes_ventas.py
from pathlib import Path
import pandas as pd
from funciones.formatear import to_snake


## Creación del DF a partir de un archivo de Ventas de Mis Comprobantes
def afip_df_mis_comprobantes_ventas_xlsx(archivo : Path) -> pd.DataFrame:
    cuit = pd.read_excel(archivo)
    cuit = str(cuit.columns[0].split(' - ')[1].split(' ')[1])
    dtypes = {
        "Tipo": "string",
        "Punto de Venta": "string",
        "Número Desde": "string",
        "Número Hasta": "string",
        "Cód. Autorización": "string",
        "Tipo Doc. Receptor": "string",
        "Nro. Doc. Receptor": "string",
        "Denominación Receptor": "string",
        "Tipo Cambio": "Float64",
        "Moneda": "string",
        "Neto Grav. IVA 0%": "Float64",
        "IVA 2,5%": "Float64",
        "Neto Grav. IVA 2,5%": "Float64",
        "IVA 5%": "Float64",
        "Neto Grav. IVA 5%": "Float64",
        "IVA 10,5%": "Float64",
        "Neto Grav. IVA 10,5%": "Float64",
        "IVA 21%": "Float64",
        "Neto Grav. IVA 21%": "Float64",
        "IVA 27%": "Float64",
        "Neto Grav. IVA 27%": "Float64",
        "Neto Gravado Total": "Float64",
        "Neto No Gravado": "Float64",
        "Op. Exentas": "Float64",
        "Otros Tributos": "Float64",
        "Total IVA": "Float64",
        "Imp. Total": "Float64",
    }
    df = pd.read_excel(archivo, skiprows=1, dtype=dtypes)
    df.rename(columns={c: to_snake(c) for c in df.columns}, inplace=True)
    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True)
    df["cuit"] = pd.Series([cuit] * len(df), dtype="string")
    return df
    
archivo = ""
df = afip_df_mis_comprobantes_ventas_xlsx(archivo)
df.head()
