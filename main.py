# Punto de entrada y ejecución
from cargador import Cargador
from limpiador import Limpiador


def main():
    df = Cargador("grupo01_marvel_comics.csv")
    limpiador = Limpiador()
    df=df.cargar()
    df=limpiador.limpiar(df)
    
    print(df.head())


if __name__ == "__main__":
    main()
