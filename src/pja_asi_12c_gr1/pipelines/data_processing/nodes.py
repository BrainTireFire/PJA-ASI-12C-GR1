"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

import pandas as pd
import opendatasets as od

from typing import Any, Tuple
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def clean_data(study_performance: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    try:
        df = study_performance
        # Here cleaning steps can be added
        print('Data cleaning completed')
        X = df.drop(columns=['math_score'], axis=1)
        y = df['math_score']
        X_processed = preprocess_data(X)
        return X_processed, y
    except Exception as e:
        print(f"Error occurred while cleaning the data: {str(e)}")
        return None, None

def preprocess_data(X: pd.DataFrame) -> Any:
    try:
        num_features = X.select_dtypes(exclude="object").columns
        cat_features = X.select_dtypes(include="object").columns

        numeric_transformer = StandardScaler()
        oh_transformer = OneHotEncoder()

        preprocessor = ColumnTransformer(
            [
                ("OneHotEncoder", oh_transformer, cat_features),
                ("StandardScaler", numeric_transformer, num_features),        
            ]
        )

        X_processed = preprocessor.fit_transform(X)
        
        return X_processed
    except Exception as e:
        print(f"Error occurred while preprocessing the data: {str(e)}")
        return None

def download_dataset(url: str, destination: str) -> None:
    try:
        od.download(url, destination)
        print('Dataset downloaded and extracted successfully')
    except Exception as e:
        print(f"Error occurred while downloading the dataset: {str(e)}")