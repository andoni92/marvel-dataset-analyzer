# Punto de entrada y ejecución
from cargador import Cargador
from limpiador import Limpiador


def main():
    df = Cargador("grupo01_marvel_comics.csv")
    limpiador = Limpiador()
    df=df.cargar()
    df=limpiador.limpiar_vacias(df)
    df=limpiador.limpiar_tuplas(df)
    df=limpiador.normalizar_columnas(df)
    
    print(df.head())


if __name__ == "__main__":
    main()
