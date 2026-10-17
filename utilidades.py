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


def imprimir_resultados(resultados: dict) -> None:
    print("\n--- Resultados del análisis ---")
    print("\nPersonajes por alineamiento (%):")
    print(resultados["porcentaje_alineamiento"].to_string())
    print("\nEstadísticas de apariciones:")
    for clave, valor in resultados["estadisticas_apariciones"].items():
        print(f"  {clave}: {valor:.2f}")
    print("\nMedia de apariciones por alineamiento:")
    print(resultados["apariciones_alineamiento"].round(2).to_string())
    print("\nPersonajes vivos por alineamiento (%):")
    print(resultados["vivos_alineamiento"].to_string())
    print("\nTop personajes por apariciones:")
    print(resultados["top"].to_string(index=False))
    print("\nTop villanos por apariciones:")
    print(resultados["top_villanos"].to_string(index=False))
