# Estadísticas y consultas
import pandas as pd
import numpy as np
from excepciones import ColumnaInexistenteError
    
    
class AnalizadorBase:
    
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Se esperaba un pandas DataFrame.")
        self._df = df.copy()
    
    @property
    def datos(self) -> pd.DataFrame:
        return self._df
    
    def validar_columnas(self, *columnas: str) -> None:
        columnas_faltantes = [col for col in columnas if col not in self._df.columns]
        if columnas_faltantes:
            raise ColumnaInexistenteError(
                f"Las siguientes columnas no existen en el dataset: {columnas_faltantes}"
            )
    
    def filtrar(self, **condiciones) -> pd.DataFrame:
        df_filtrado = self._df
        for columna, valor in condiciones.items():
            self.validar_columnas(columna)
            df_filtrado = df_filtrado[df_filtrado[columna] == valor]
        return df_filtrado
    
    
class AnalizadorMarvel(AnalizadorBase):
    
    def __init__(self, df: pd.DataFrame):
        super().__init__(df)
    
    def distribucion_alineamiento(self) -> pd.Series:
        self.validar_columnas("align")
        # Cuenta frecuencias excluyendo nulos o agrupándolos
        return self.datos["align"].dropna().value_counts()
    
    def evolucion_primeras_apariciones(self) -> pd.Series:
        self.validar_columnas("year")
        # Filtrar valores válidos de año y agrupar ordenadamente
        serie_anios = self.datos["year"].dropna().astype(int)
        return serie_anios.value_counts().sort_index()
    
    def top_personajes_apariciones(self, n: int = 10) -> pd.DataFrame:
        self.validar_columnas("name", "appearances")
        df_sub = self.datos.dropna(subset=["appearances"])
        return (
            df_sub[["name", "appearances"]]
            .sort_values(by="appearances", ascending=False)
            .head(n)
        )
    
    def apariciones_por_alineamiento(self) -> pd.Series:
        self.validar_columnas("align", "appearances")
        return (
            self.datos.dropna(subset=["align", "appearances"])
            .groupby("align")["appearances"]
            .mean()
            .sort_values(ascending=False)
        )
    
    
if __name__ == "__main__":
    # Prueba autónoma con el CSV original
    df_raw = pd.read_csv("grupo01_marvel_comics.csv")
    analizador = AnalizadorMarvel(df_raw)
    print("--- Distribución Alineamiento ---")
    print(analizador.distribucion_alineamiento())
    print("\n--- Top 5 Personajes ---")
    print(analizador.top_personajes_apariciones(n=5))