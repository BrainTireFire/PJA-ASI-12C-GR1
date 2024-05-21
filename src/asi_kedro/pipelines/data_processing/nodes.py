"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""
import pandas as pd
import numpy as np
from typing import  Tuple
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from typing import Any

def separate_dependent_variable(study_performance: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    try:
        df = study_performance
        # Here cleaning steps can be added
        X = df.drop(columns=['math_score'], axis=1)
        y = df['math_score']
        return X, y
    except Exception as e:
        print(f"Error occurred while separating dependent variable: {str(e)}")
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
        # X_processed = pd.DataFrame(X_processed, index=X.index, columns=X.columns);
            
        return X_processed
    except Exception as e:
        print(f"Error occurred while preprocessing the data: {str(e)}")
        return None

def split_data(X: np.ndarray, y: np.ndarray, params_data_split) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    test_size = params_data_split['test_size']
    random_state = params_data_split["random_state"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test