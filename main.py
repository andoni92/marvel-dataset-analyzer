# Punto de entrada y ejecución
import os
from cargador import Cargador
from limpiador import Limpiador
from analizador import AnalizadorMarvel
from visualizador import VisualizadorMarvel
from excepciones import DatasetInvalidoError, ColumnaInexistenteError
from utilidades import imprimir_informe


def main(ruta: str = "grupo01_marvel_comics.csv"):
    try:
        df = Cargador(ruta).cargar()
        limpiador = Limpiador()
        df = limpiador.limpiar(df)
        imprimir_informe(limpiador.informe)
        resultados = AnalizadorMarvel(df).analizar()

        visualizador = VisualizadorMarvel()
        visualizador.generar_graficos(resultados)
        df.to_csv(os.path.join(visualizador.carpeta_salida, "marvel_limpio.csv"), index=False)

    except DatasetInvalidoError as error:
        print(f"Error en la carga o validación: {error}")

    except ColumnaInexistenteError as error:
        print(f"Error durante el análisis: {error}")

    else:
        print("Pipeline ejecutado correctamente.")

    finally:
        print("Fin de la ejecución.")


if __name__ == "__main__":
    main()
