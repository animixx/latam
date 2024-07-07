from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Cargar el JSON directamente en un DataFrame
    tweets = pd.read_json(file_path, lines=True)
    
    # Extraer el nombre de usuario usando una función vectorizada que es mas rapido que iterar manualmente
    tweets['username'] = tweets['user'].apply(lambda x: x['username'])
    
    # Convertir la columna 'date' a solo fecha, sin necesidad de una columna intermedia
    tweets['date'] = pd.to_datetime(tweets['date']).dt.date
    
    # Agrupar por 'date' y 'username', contar los tweets, y sumar los totales por día
    resultado = tweets.groupby(['date', 'username']).size().reset_index(name='cuenta')
    
    # Obtener el usuario más activo por día
    resultado = resultado.loc[resultado.groupby('date')['cuenta'].idxmax()]
    
    # Ordenar por 'cuenta' para obtener los 10 días con más actividad
    resultado = resultado.sort_values(by='cuenta', ascending=False).head(10)
    
    # Devolver el resultado como una lista de tuplas
    return list(resultado[['date', 'username']].itertuples(index=False, name=None))