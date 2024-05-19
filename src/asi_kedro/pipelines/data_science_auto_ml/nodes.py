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
from autogluon.tabular import TabularPredictor, TabularDataset

def split_data(fullSet: pd.DataFrame, params_data_split) -> Tuple[pd.DataFrame, pd.DataFrame]:
    test_size = params_data_split['test_size']
    random_state = params_data_split["random_state"]
    
    fullSet_train, fullSet_test = train_test_split(fullSet, test_size=test_size, random_state=random_state)

    return fullSet_train, fullSet_test


def train_model_auto_ml(train_data: pd.DataFrame, validate_data: pd.DataFrame, params_auto_ml) -> TabularPredictor:
    try:
        # train_data = TabularDataset(params_auto_ml.get('file_path', 'data/01_raw/study_performance.csv'))
        label_column = params_auto_ml.get('label_column', 'math_score')
        output_directory = params_auto_ml.get('output_directory', 'models/auto_ml')

        # Additional parameters
        hyperparameters = params_auto_ml.get('hyperparameters', 'default')
        presets = params_auto_ml.get('presets', 'best_quality')
        time_limit = params_auto_ml.get('time_limit', 3600)
        problem_type = params_auto_ml.get('problem_type', 'regression')

        predictor = TabularPredictor(label=label_column, problem_type=problem_type, path=output_directory)
        predictor.fit(train_data=train_data, tuning_data=validate_data, hyperparameters=hyperparameters, presets=presets,
                      time_limit=time_limit, use_bag_holdout=True, keep_only_best=True)
        
        return predictor
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None
    


def evaluate_model_auto_ml(predictor: TabularPredictor, test_data: pd.DataFrame, params_auto_ml) -> Any:
    try:
        # test_data = TabularDataset(params_auto_ml.get('file_path', 'data/01_raw/study_performance.csv'))
        results = predictor.evaluate(test_data)
        print(predictor.leaderboard(test_data, silent=True))
        return results
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return {}