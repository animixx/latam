from typing import List, Tuple
import pandas as pd
import re
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Cargar el JSON directamente en un DataFrame
    tweets = pd.read_json(file_path, lines=True)
    menciones_counter = Counter()
    
    #Se itera sobre cada mensaje en la columna 'content' del dataframe
    for msg in tweets['content']:
        #ocupando regex se buscan todas las palabra que comiencen con @
        menciones = re.findall(r"@(\w+)", msg)
        menciones_counter.update(menciones)
    
    return menciones_counter.most_common(10)