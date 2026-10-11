# Limpieza y transformación
import pandas as pd
class Limpiador:
    def __init__(self):
        pass
#Rellena los vacios de las columnas de texto con "Desconocido"; las numericas se quedan como NaN
    def limpiar_vacias(self, df: pd.DataFrame):
        columnas_texto = []
        for u in df.columns:
            if pd.api.types.is_string_dtype(df[u]):
                columnas_texto.append(u)    
          df[columnas_texto] = df[columnas_texto].fillna('Desconocido')
        return df
        

#Limpia los caracteres especiales de las columnas de texto y convierte las columnas numericas a enteros
    def limpiar_tuplas(self, df: pd.DataFrame):
        columnas= df.columns
        for u in columnas:
            if pd.api.types.is_string_dtype(df[u]):
                df[u] = df[u].str.strip()
            if pd.api.types.is_numeric_dtype(df[u]):
                df[u] = df[u].astype('Int64')
        return df
#Normaliza los nombres de las columnas
    def normalizar_columnas(self, df: pd.DataFrame):
        df.columns = df.columns.str.strip().str.replace(' ','_').str.replace(r'[^a-zA-ZñÑ_0-9]','',regex=True).str.lower()
        return df

    def decodificar_nombres(self, df: pd.DataFrame):
        tiene_codigo = df['name'].str.contains('\\u', regex=False)
        indices = df.index[tiene_codigo]

        for i in indices:
            texto = df.at[i, 'name']
            posicion = texto.find('\\u')

            while posicion != -1:
                codigo = texto[posicion + 2 : posicion + 6]
                letra = chr(int(codigo, 16))
                texto = texto[:posicion] + letra + texto[posicion + 6:]
                posicion = texto.find('\\u')

            df.at[i, 'name'] = texto

        df['name'] = df['name'].str.replace('\\"', '"', regex=False)
        return df


    def convertir_fecha(self, df: pd.DataFrame):
        mes = df['first_appearance'].where(df['first_appearance'] != 'Desconocido').str[:3]
        df['first_appearance'] = pd.to_datetime(mes + '-' + df['year'].astype('string'),
                                                format='%b-%Y', errors='coerce')
        return df

    def normalizar_categorias(self, df: pd.DataFrame):
        df = df.drop(columns=['urlslug'])
        df = df.dropna(subset=['alive'])
        df['gsm'] = df['gsm'].fillna('No especificado')

        sufijos = {'align': ' Characters', 'sex': ' Characters', 'gsm': ' Characters',
                   'alive': ' Characters', 'eye': ' Eyes', 'hair': ' Hair', 'id': ' Identity'}
        for columna, sufijo in sufijos.items():
            df[columna] = df[columna].str.removesuffix(sufijo)

        df['eye'] = df['eye'].str.replace(' Eyeballs', '', regex=False)
        df['hair'] = df['hair'].replace({'Bald': 'Sin pelo', 'No': 'Sin pelo'})
        return df

    def limpiar(self, df: pd.DataFrame):
        df = self.decodificar_nombres(df)
        df = self.normalizar_columnas(df)
        df = self.normalizar_categorias(df)
        df = self.limpiar_vacias(df)
        df = self.limpiar_tuplas(df)
        df = self.convertir_fecha(df)
        return df