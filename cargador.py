# Lectura y validación del CSV
import pandas as pd
from excepciones import DatasetInvalidoError


class Cargador:
    def __init__(self, ruta: str):
        self.__ruta = ruta

    @property
    def ruta(self) -> str:
        return self.__ruta

    def cargar(self) -> pd.DataFrame:
        try:
             df=pd.read_csv(self.__ruta)
        except FileNotFoundError as e:
            raise DatasetInvalidoError(f"No se pudo leer '{self.__ruta}'") from e
        else:
            return df
