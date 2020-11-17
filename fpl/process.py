import pandas as pd
import numpy as np
from typing import Iterable, Optional, Dict

def df_from_json(json_obj: Dict, fields: Optional[Iterable[str]] = None) -> pd.DataFrame:
    """Returns a pandas DataFrame from the given JSON object.

    The DataFrame is optionally filtered to only contain the given fields.

    Arguments:
        json_obj {dict} -- The JSON object to transform into a DataFrame.

        fields {Iterable[str]} -- Fields to include in the DataFrame (default
                                  to all fields if None). If a field doesn't
                                  appear in the JSON, it's dropped.
                                  TODO: Do we want to drop, or raise an exc?
    """
    df = pd.DataFrame(json_obj)
    if fields is not None:
        #assert(all([field in json_obj for field in fields]))
        df = df[[f for f in fields if f in json_obj]]

    return df



