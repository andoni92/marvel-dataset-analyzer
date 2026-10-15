# Errores personalizados
class PipelineError(Exception):
    """Clase base de todos los errores esperables del pipeline."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.__mensaje = mensaje

    @property
    def mensaje(self) -> str:
        return self.__mensaje


class DatasetInvalidoError(PipelineError):
    """Lanzada cuando el fichero no se puede leer o su contenido no es válido."""

    def __init__(self, mensaje: str, ruta: str = None):
        if ruta is not None:
            mensaje = f"{mensaje} (fichero: '{ruta}')"
        super().__init__(mensaje)
        self.__ruta = ruta

    @property
    def ruta(self) -> str:
        return self.__ruta


class ColumnaInexistenteError(PipelineError):
    """Lanzada cuando se solicita una o varias columnas que no existen en el DataFrame."""

    def __init__(self, columnas: list):
        super().__init__(f"Las siguientes columnas no existen en el dataset: {columnas}")
        self.__columnas = list(columnas)

    @property
    def columnas(self) -> list:
        return self.__columnas
    