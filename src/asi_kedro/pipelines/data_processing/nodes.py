"""
This is a boilerplate pipeline 'data_processing_2'
generated using Kedro 0.19.3
"""

from typing import Any, Tuple
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder



def preprocess_data(dataset: pd.DataFrame) -> pd.DataFrame:
    try:
        num_features = dataset.select_dtypes(exclude="object").columns
        cat_features = dataset.select_dtypes(include="object").columns

        # Initialize transformers
        numeric_transformer = StandardScaler()
        label_encoders = {col: LabelEncoder() for col in cat_features}

        # Scale numeric features
        scaled_dataset = numeric_transformer.fit_transform(dataset[num_features])
        scaled_dataset = pd.DataFrame(scaled_dataset, columns=num_features)

        # Encode categorical features
        encoded_datasets = []
        for col in cat_features:
            encoded_col = label_encoders[col].fit_transform(dataset[col])
            encoded_datasets.append(pd.DataFrame(encoded_col, columns=[col]))

        encoded_dataset = pd.concat(encoded_datasets, axis=1)

        # Concatenate scaled numeric and encoded categorical features
        dataset_processed = pd.concat([scaled_dataset, encoded_dataset], axis=1)
        
        print(dataset_processed)   
        return dataset_processed
    
    except Exception as e:
        print(f"Error occurred while preprocessing the data: {str(e)}")
        return None
    

def split_data(data: pd.DataFrame, params_data_split) -> Tuple[pd.DataFrame, pd.DataFrame]:
    test_size = params_data_split['test_size']
    random_state = params_data_split["random_state"]
    
    data_train, data_test = train_test_split(data, test_size=test_size, random_state=random_state)
    print(isinstance(data_test, pd.DataFrame))
    return data_train, data_test
