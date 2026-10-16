# Lectura y validación del CSV
import pandas as pd
from excepciones import DatasetInvalidoError

COLUMNAS_REQUERIDAS = ("page_id", "name", "urlslug", "ID", "ALIGN", "EYE", "HAIR", "SEX",
                       "GSM", "ALIVE", "APPEARANCES", "FIRST APPEARANCE", "Year")
COLUMNAS_NUMERICAS = ("APPEARANCES", "Year")


class Cargador:
    def __init__(self, ruta: str, columnas_requeridas: tuple = COLUMNAS_REQUERIDAS):
        self.__ruta = ruta
        self.__columnas_requeridas = columnas_requeridas

    @property
    def ruta(self) -> str:
        return self.__ruta

    @property
    def columnas_requeridas(self) -> tuple:
        return self.__columnas_requeridas

    def cargar(self) -> pd.DataFrame:
        try:
             df=pd.read_csv(self.__ruta)
        except (FileNotFoundError, PermissionError) as e:
            raise DatasetInvalidoError("No se pudo leer el archivo", self.__ruta) from e
        except pd.errors.EmptyDataError as e:
            raise DatasetInvalidoError("El archivo está vacío", self.__ruta) from e
        except (pd.errors.ParserError, UnicodeDecodeError) as e:
            raise DatasetInvalidoError("El archivo no tiene un formato CSV válido", self.__ruta) from e
        else:
            self.__validar(df)
            return df

    def __validar(self, df: pd.DataFrame) -> None:
        if df.empty:
            raise DatasetInvalidoError("El archivo no contiene registros", self.__ruta)

        faltantes = [col for col in self.__columnas_requeridas if col not in df.columns]
        if faltantes:
            raise DatasetInvalidoError(f"Faltan columnas necesarias: {faltantes}", self.__ruta)

        for col in COLUMNAS_NUMERICAS:
            if col in df.columns and not pd.api.types.is_numeric_dtype(df[col]):
                raise DatasetInvalidoError(f"La columna '{col}' no es numérica", self.__ruta)
