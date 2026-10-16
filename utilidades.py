# Funciones auxiliares reutilizables
import pandas as pd


def resumen_calidad(df: pd.DataFrame) -> dict:
    return {
        "filas": df.shape[0],
        "columnas": df.shape[1],
        "duplicados": int(df.duplicated().sum()),
        "nulos": df.isna().sum(),
        "tipos": df.dtypes.astype(str),
    }


def imprimir_informe(informe: dict) -> None:
    antes, despues = informe["antes"], informe["despues"]
    print("--- Informe de calidad ---")
    print(f"Filas: {antes['filas']} -> {despues['filas']}")
    print(f"Columnas: {antes['columnas']} -> {despues['columnas']}")
    print(f"Duplicados detectados: {antes['duplicados']} | eliminados: {informe['duplicados_eliminados']}")
    print("\nAntes de limpiar:")
    print(pd.DataFrame({"nulos": antes["nulos"], "tipo": antes["tipos"]}))
    print("\nDespués de limpiar:")
    print(pd.DataFrame({"nulos": despues["nulos"], "tipo": despues["tipos"]}))
    print("\nTransformaciones aplicadas:", ", ".join(informe["transformaciones"]))
