import sys
from deducciones.misiones         import deducciones_misiones
from impuestos.monotributo_simple import liquidar_monotributo_simple
from bdd.funciones_db             import importar_schema
from bdd.datos.importar_datos     import importar_datos

def main():
    if len(sys.argv) < 2:
        raise Exception(f"Por favor especificá qué querés hacer:\n {comandos}")
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print(comandos)
        return
    if sys.argv[1] == "--dgr":
        deducciones_misiones()
        return
    if sys.argv[1] == "--mono_simple":
        liquidar_monotributo_simple()
        return
    if sys.argv[1] == "--bdd":
        importar_schema()
        if sys.argv[2] == "datos":
            importar_datos()
        return
    else:
        raise Exception(f"Ese no es un comando válido.\n {comandos}")

comandos = """
    Comandos disponibles:
    --dgr (Descargar deducciones de Misiones)
    --help
    --mono_simple (Presentar el monotributo simplificado)
    --bdd (Actualizar la base de datos de las ventas)
    """

if __name__ == "__main__":
    main()
