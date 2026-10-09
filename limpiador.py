# Limpieza y transformación
import pandas as pd
class Limpiador:
    def __init__(self):
        pass
#Rellena los vacios de las columnas de texto con "Desconocido"; las numericas se quedan como NaN
    def limpiar_vacias(self, df: pd.DataFrame):
        columnas_texto = ['ID', 'ALIGN', 'EYE', 'HAIR', 'SEX', 'GSM', 'ALIVE', 'FIRST APPEARANCE']
        return df.fillna({columna: 'Desconocido' for columna in columnas_texto})

#Limpia los caracteres especiales de las columnas de texto y convierte las columnas numericas a enteros
    def limpiar_tuplas(self, df: pd.DataFrame):
        columnas= df.columns
        for u in columnas:
            if pd.api.types.is_string_dtype(df[u]):
                df[u] = df[u].astype(str).str.replace(r'[^a-zA-ZñÑ()-]', '', regex=True)
            if pd.api.types.is_numeric_dtype(df[u]):
                df[u] = df[u].astype('Int64')
        return df
#Normaliza los nombres de las columnas
    def normalizar_columnas(self, df: pd.DataFrame):
        df.columns = df.columns.str.strip().str.replace(' ','_').str.replace(r'[^a-zA-ZñÑ_0-9]','',regex=True).str.lower()
        return df


            