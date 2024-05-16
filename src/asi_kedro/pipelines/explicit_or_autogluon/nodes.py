"""
This is a boilerplate pipeline 'explicit_or_autogluon'
generated using Kedro 0.19.3

"""

import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from typing import Any

def split_data(fullSet: pd.DataFrame, params_data_split) -> Tuple[np.ndarray, np.ndarray]:
    test_size = params_data_split['test_size']
    random_state = params_data_split["random_state"]
    
    fullSet_train, fullSet_test = train_test_split(fullSet, test_size=test_size, random_state=random_state)

    return fullSet_train, fullSet_test