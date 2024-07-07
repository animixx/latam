from typing import List, Tuple
import pandas as pd
import emoji
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Cargar el JSON directamente en un DataFrame
    tweets = pd.read_json(file_path, lines=True)
    
    emoji_counter = Counter()
    
    #Se itera sobre cada mensaje en la columna 'content' del dataframe
    for msg in tweets['content']:
        emojis = emoji.emoji_list(msg)
        for x in emojis:
            #por cada uno de los emoji encontrados, se aumenta el contador
            emoji_counter[x['emoji']] += 1
    
    return emoji_counter.most_common(10)
