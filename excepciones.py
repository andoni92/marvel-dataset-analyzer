# Errores personalizados
class PipelineError(Exception):
    pass

class DatasetInvalidoError(PipelineError):
    pass

class DatasetInvalidoError(Exception):
    """Lanzada cuando la estructura o contenido del dataset no es válida."""
    pass
    
class ColumnaInexistenteError(Exception):
    """Lanzada cuando se solicita una columna que no existe en el DataFrame."""
    pass