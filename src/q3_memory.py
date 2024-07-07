from typing import List, Tuple
import pandas as pd
import re
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Especificar tipos de datos para optimizar la carga de memoria
    dtype = {'user': 'object'}
    tweets = pd.read_json(file_path, lines=True, dtype=dtype)
    menciones_counter = Counter()
    
    #Se itera sobre cada mensaje en la columna 'content' del dataframe
    for msg in tweets['content']:
        #ocupando regex se buscan todas las palabra que comiencen con @
        menciones = re.findall(r"@(\w+)", msg)
        menciones_counter.update(menciones)
    
    return menciones_counter.most_common(10)