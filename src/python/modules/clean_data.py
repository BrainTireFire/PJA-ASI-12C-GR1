import pandas as pd
from modules.preprocess_data import preprocess_data
from typing import Tuple

def clean_data(data_path: str) -> Tuple[pd.DataFrame, pd.Series]:
    try:
        df = pd.read_csv(data_path)
        # Here cleaning steps can be added
        print('Data cleaning completed')
        X = df.drop(columns=['math_score'], axis=1)
        y = df['math_score']
        X_processed = preprocess_data(X)
        return X_processed, y
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None, None