"""
This is a boilerplate pipeline 'data_science_2'
generated using Kedro 0.19.3
"""

from typing import Tuple
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor, TabularDataset
import wandb as wb




def train_model_auto_ml(train_data: pd.DataFrame, params_auto_ml) -> TabularPredictor:
    try:
        print('train_model_auto_ml')
        print(isinstance(train_data, pd.DataFrame))
        # train_data = TabularDataset(params_auto_ml.get('file_path', 'data/01_raw/study_performance.csv'))
        label_column = params_auto_ml.get('label_column', 'math_score')

        # Additional parameters
        hyperparameters = params_auto_ml.get('hyperparameters', 'default')
        presets = params_auto_ml.get('presets', 'best_quality')
        time_limit = params_auto_ml.get('time_limit', 3600)
        problem_type = params_auto_ml.get('problem_type', 'regression')

        train_data = TabularDataset(train_data)

        predictor = TabularPredictor(label=label_column, problem_type=problem_type, path="data/06_models/challenger")
        predictor.fit(train_data=train_data, hyperparameters=hyperparameters, presets=presets,
                      time_limit=time_limit, keep_only_best=True)
        
        return predictor
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None
    
def evaluate(challenger: TabularPredictor, data_test: pd.DataFrame):
    r2 = -challenger.evaluate(data_test)['root_mean_squared_error']
    return r2
    
def sendDataToWB(results_challenger, params_model) -> None:
    key = params_model.get("wbKey");
    print(key)
    if key != "notprovided":
        wb.login(key=params_model.get("wbKey"))
        wb.init(
        # Set the project where this run will be logged
        project=params_model.get("project_name", "PJA-ASI-12C-GR1"),
        )
        wb.log({'r2': results_challenger})
        wb.finish()
    else:
        print("No Weights&Biases key provided")
