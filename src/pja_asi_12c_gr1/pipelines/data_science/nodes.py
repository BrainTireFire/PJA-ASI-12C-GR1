"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from joblib import dump
from typing import Any, Tuple

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def plot_scatter(y_test: np.ndarray, y_pred: np.ndarray) -> None:
    try:
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.show() 
    except Exception as e:
        print(f"Error occurred while plotting scatter plot: {str(e)}")

def evaluate_model(true: np.ndarray, predicted: np.ndarray) -> Tuple[float, float, float]:
    try:
        mae = mean_absolute_error(true, predicted)
        mse = mean_squared_error(true, predicted)
        rmse = np.sqrt(mse)
        r2_square = r2_score(true, predicted)
        return mae, rmse, r2_square
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None, None, None
    
def train_model(X: np.ndarray, y: np.ndarray) -> Tuple[LinearRegression, np.ndarray, np.ndarray]:
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression(fit_intercept=True)
        model.fit(X_train, y_train)
        return model, X_test, y_test
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None, None, None

def save_model(model: Any, output_dir: str) -> None:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        dump(model, os.path.join(output_dir, 'model.joblib'))
        print("Model saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving the model: {str(e)}")