"""
This is a boilerplate pipeline 'data_science_auto_ml'
generated using Kedro 0.19.3
"""
import pandas as pd
from typing import Any
from autogluon.tabular import TabularPredictor, TabularDataset

def train_model_auto_ml(params_auto_ml) -> TabularPredictor:
    try:
        train_data = TabularDataset(params_auto_ml.get('file_path', 'data/01_raw/study_performance.csv'))
        label_column = params_auto_ml.get('label_column', 'race_ethnicity')
        output_directory = params_auto_ml.get('output_directory', 'models/auto_ml')

        predictor = TabularPredictor(label=label_column, path=output_directory).fit(
            train_data
        )
        return predictor
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None

def evaluate_model_auto_ml(predictor: TabularPredictor, params_auto_ml) -> Any:
    try:
        train_data = TabularDataset(params_auto_ml.get('file_path', 'data/01_raw/study_performance.csv'))
        results = predictor.evaluate(train_data)
        return results
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return {}