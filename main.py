import sys
from deducciones.misiones import deducciones_misiones

def main():
    if len(sys.argv) < 2:
        raise Exception(f"Por favor especificá qué querés hacer:\n {comandos}")
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print(comandos)
        return
    if sys.argv[1] == "--dgr":
        deducciones_misiones()
    raise Exception(f"Ese no es un comando válido.\n {comandos}")

comandos = """
    Comandos disponibles:
    --dgr
    --help
    """

if __name__ == "__main__":
    main()
