import sys
from deducciones.misiones         import deducciones_misiones
from impuestos.monotributo_simple import liquidar_monotributo_simple

def main():
    if len(sys.argv) < 2:
        raise Exception(f"Por favor especificá qué querés hacer:\n {comandos}")
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print(comandos)
        return
    if sys.argv[1] == "--dgr":
        deducciones_misiones()
    if sys.argv[1] == "--mono_simple":
        liquidar_monotributo_simple()

    raise Exception(f"Ese no es un comando válido.\n {comandos}")

comandos = """
    Comandos disponibles:
    --dgr
    --help
    --mono_simple
    """

if __name__ == "__main__":
    main()
