import pandas as pd
from pandas.core.frame import DataFrame
from typing import Dict, List

def convert_dict_to_df(table: Dict[str, List[int]]) -> DataFrame:
    return pd.DataFrame(table)
