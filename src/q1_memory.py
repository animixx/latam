from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Especificar tipos de datos para optimizar la carga de memoria
    dtype = {'user': 'object'}
    tweets = pd.read_json(file_path, lines=True, dtype=dtype)
    
    # Extraer directamente el username en una lista usando comprensión de listas para eficiencia
    tweets['username'] = [user['username'] for user in tweets['user']]
    
    # Convertir la columna 'date' a fecha y extraer solo la fecha para reducir el uso de memoria
    tweets['date'] = pd.to_datetime(tweets['date']).dt.date
    
    # Agrupar por 'date' y 'username', contar, y luego sumar los totales por día en una operación
    resultado = (tweets.groupby(['date', 'username'])
                 .size()
                 .reset_index(name='cuenta')
                 .sort_values(['date', 'cuenta'], ascending=[True, False])
                 .drop_duplicates(subset=['date'], keep='first')
                 .nlargest(10, 'cuenta'))

    # Convertir el resultado final a la lista de tuplas esperada sin columnas intermedias
    return list(resultado[['date', 'username']].itertuples(index=False, name=None))