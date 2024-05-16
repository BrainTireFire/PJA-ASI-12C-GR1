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

        # Additional parameters
        hyperparameters = params_auto_ml.get('hyperparameters', 'multimodal')
        presets = params_auto_ml.get('presets', 'best_quality')
        time_limit = params_auto_ml.get('time_limit', 3600)

        predictor = TabularPredictor(label=label_column, path=output_directory)
        predictor.fit(train_data, hyperparameters=hyperparameters, presets=presets,
                      time_limit=time_limit)
        
        return predictor
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None

def evaluate_model_auto_ml(predictor: TabularPredictor, params_auto_ml) -> Any:
    try:
        train_data = TabularDataset(params_auto_ml.get('file_path', 'data/01_raw/study_performance.csv'))
        results = predictor.evaluate(train_data)
        print(predictor.leaderboard(train_data, silent=True))
        return results
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return {}