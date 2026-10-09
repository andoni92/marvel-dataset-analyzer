# Errores personalizados
class PipelineError(Exception):
    pass

class DatasetInvalidoError(PipelineError):
    pass