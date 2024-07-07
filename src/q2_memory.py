from typing import List, Tuple
import pandas as pd
import emoji
from collections import Counter

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Especificar tipos de datos para optimizar la carga de memoria
    dtype = {'user': 'object'}
    tweets = pd.read_json(file_path, lines=True, dtype=dtype)
    
    # Extraer todos los emojis de todos los tweets usando comprensión de lista y emoji.emoji_list
    all_emojis = [x['emoji'] for msg in tweets['content'] for x in emoji.emoji_list(msg)]
    
    # Contar la frecuencia de cada emoji usando Counter, que es más eficiente
    emoji_counts = Counter(all_emojis)
    
    # Obtener los 10 emojis más frecuentes
    most_common_emojis = emoji_counts.most_common(10)
    
    return most_common_emojis