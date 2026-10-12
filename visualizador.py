# Creación y guardado de gráficos
import os
import matplotlib.pyplot as plt
import pandas as pd

class VisualizadorMarvel:
    
    def __init__(self, carpeta_salida: str = "resultados"):
        self._carpeta_salida = carpeta_salida
        os.makedirs(self._carpeta_salida, exist_ok=True)
    
    @property
    def carpeta_salida(self) -> str:
        return self._carpeta_salida
    
    def grafico_alineamiento(self, serie: pd.Series, nombre_archivo: str = "alineamiento.png") -> str:
        fig, ax = plt.subplots(figsize=(8, 5))
        serie.plot(kind="bar", ax=ax, color="#1f77b4", edgecolor="black")
        ax.set_title("Distribución de Personajes por Alineamiento", fontsize=14, fontweight="bold")
        ax.set_xlabel("Alineamiento", fontsize=12)
        ax.set_ylabel("Número de Personajes", fontsize=12)
        ax.tick_params(axis="x", rotation=15)
        plt.tight_layout()
    
        ruta = os.path.join(self._carpeta_salida, nombre_archivo)
        fig.savefig(ruta, dpi=300)
        plt.close(fig)
        return ruta
    
    def grafico_evolucion_anual(self, serie: pd.Series, nombre_archivo: str = "personajes_por_anio.png") -> str:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(serie.index, serie.values, color="#e63946", linewidth=2)
        ax.set_title("Primeras Apariciones de Personajes por Año (Marvel)", fontsize=14, fontweight="bold")
        ax.set_xlabel("Año de Debut", fontsize=12)
        ax.set_ylabel("Nuevos Personajes Registrados", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
    
        ruta = os.path.join(self._carpeta_salida, nombre_archivo)
        fig.savefig(ruta, dpi=300)
        plt.close(fig)
        return ruta
    
    def grafico_top_apariciones(self, df_top: pd.DataFrame, nombre_archivo: str = "top_personajes_apariciones.png") -> str:
        fig, ax = plt.subplots(figsize=(12, 6))
        # Invertir para que el personaje #1 quede arriba
        df_ordenado = df_top.sort_values(by="appearances", ascending=True)
        ax.barh(df_ordenado["name"], df_ordenado["appearances"], color="#2a9d8f", edgecolor="black")
        ax.set_title("Top Personajes de Marvel con Mayor Número de Apariciones", fontsize=14, fontweight="bold")
        ax.set_xlabel("Número de Apariciones", fontsize=12)
        ax.set_ylabel("Personaje", fontsize=12)
        plt.tight_layout()
    
        ruta = os.path.join(self._carpeta_salida, nombre_archivo)
        fig.savefig(ruta, dpi=300)
        plt.close(fig)
        return ruta


if __name__ == "__main__":
    from analizador import AnalizadorMarvel
    df_raw = pd.read_csv("grupo01_marvel_comics.csv")
    analizador = AnalizadorMarvel(df_raw)
    vis = VisualizadorMarvel()

    vis.grafico_alineamiento(analizador.distribucion_alineamiento())
    vis.grafico_evolucion_anual(analizador.evolucion_primeras_apariciones())
    vis.grafico_top_apariciones(analizador.top_personajes_apariciones(10))
    print("Gráficos generados en la carpeta resultados/")