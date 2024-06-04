"""
This is a boilerplate pipeline 'data_science_3'
generated using Kedro 0.19.3
"""

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import wandb as wb


def train_model(data_train: pd.DataFrame, params_model) -> LinearRegression:
    try:
        model = LinearRegression(fit_intercept=params_model.get("fit_intercept", True))
        print(data_train.head())
        X = data_train.drop(columns=[params_model.get('label_column', 'math_score')], inplace=False)
        print(X.head())
        y = data_train[params_model.get('label_column', 'math_score')]
        print(y.head())
        model.fit(X, y)
        return model
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None
    
def evaluate_model(model: LinearRegression, data_test: pd.DataFrame, params_model) -> float:
    try:
        X_test = data_test.drop(columns=[params_model.get('label_column', 'math_score')], inplace=False)
        y_test = data_test[params_model.get('label_column', 'math_score')]
        predicted = model.predict(X_test)

        r2_square = r2_score(y_test, predicted)
        return r2_square
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None
    
def sendDataToWB(r2_square, params_model) -> None:
    wb.login(key="6677f668e127b3ddf8f0322696ed29f50bc3ce2e")
    wb.init(
      # Set the project where this run will be logged
      project=params_model.get("project_name", "PJA-ASI-12C-GR1"),
      )
    wb.log({"r2": r2_square})
    wb.finish()