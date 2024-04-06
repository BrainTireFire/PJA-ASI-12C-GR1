import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from typing import Any

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
