# Limpieza y transformación
import pandas as pd
class Limpiador:
    def __init__(self):
        pass
    #Rellena los vacios de las columnas de texto con "Desconocido"; las numericas se quedan como NaN
    def limpiar_vacias(self, df: pd.DataFrame):
        columnas_texto = ['ID', 'ALIGN', 'EYE', 'HAIR', 'SEX', 'GSM', 'ALIVE', 'FIRST APPEARANCE']
        return df.fillna({columna: 'Desconocido' for columna in columnas_texto})

    def limpiar_strings(df: pd.DataFrame):
        columnas= df.columns
        for u in columnas:
            if df[u].dtype=='string':
                for indice , valor in df[u].items():
                    df.loc[indice,u]= str(valor).replace(r'[^a-zA-ZñÑ()-]','',regex=True)
            if df[u].dtype == 'float64' or df[u].dtype == 'float32':
                for indice, valor in df[u].items():
                    df.loc[indice,u]= int(valor)
        return df

    def normalizar_columnas(df: pd.DataFrame):
        df.columns.str.strip().str.replace(' ','_').str.replace(r'[^a-zA-ZñÑ]','',regex=True).str.lower()
        return df


            