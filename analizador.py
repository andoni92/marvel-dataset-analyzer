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
            raise ColumnaInexistenteError(columnas_faltantes)
    
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

    def porcentaje_alineamiento(self) -> pd.Series:
        conteo = self.distribucion_alineamiento()
        valores = conteo.to_numpy()
        return pd.Series(np.round(valores / np.sum(valores) * 100, 2), index=conteo.index)

    def estadisticas_apariciones(self) -> dict:
        self.validar_columnas("appearances")
        valores = self.datos["appearances"].dropna().to_numpy(dtype=float)
        return {
            "media": np.mean(valores),
            "mediana": np.median(valores),
            "desviacion": np.std(valores),
            "percentil_90": np.percentile(valores, 90),
            "maximo": np.max(valores),
        }

    def analizar(self, n_top: int = 10) -> dict:
        return {
            "alineamiento": self.distribucion_alineamiento(),
            "porcentaje_alineamiento": self.porcentaje_alineamiento(),
            "estadisticas_apariciones": self.estadisticas_apariciones(),
            "evolucion": self.evolucion_primeras_apariciones(),
            "top": self.top_personajes_apariciones(n_top),
            "apariciones_alineamiento": self.apariciones_por_alineamiento(),
        }
    
    
if __name__ == "__main__":
    from cargador import Cargador
    from limpiador import Limpiador
    df = Limpiador().limpiar(Cargador("grupo01_marvel_comics.csv").cargar())
    analizador = AnalizadorMarvel(df)
    print("--- Distribución Alineamiento ---")
    print(analizador.distribucion_alineamiento())
    print("\n--- Top 5 Personajes ---")
    print(analizador.top_personajes_apariciones(n=5))