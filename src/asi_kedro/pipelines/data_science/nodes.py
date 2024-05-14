"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""
from sklearn.linear_model import LinearRegression
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import wandb as wb

def train_model(X: np.ndarray, y: np.ndarray, params_model) -> LinearRegression:
    try:
        model = LinearRegression(fit_intercept=params_model.get("fit_intercept", True))
        model.fit(X, y)
        return model
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None

def evaluate_model(model: LinearRegression, y_test: np.ndarray, X_test: np.ndarray, params_model) -> Tuple[float, float, float]:
    try:
        predicted = model.predict(X_test)

        mae = mean_absolute_error(y_test, predicted)
        mse = mean_squared_error(y_test, predicted)
        rmse = np.sqrt(mse)
        r2_square = r2_score(y_test, predicted)
        return mae, rmse, r2_square
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None, None, None

def plot_scatter(y_test: np.ndarray, y_pred: np.ndarray, params_model) -> None:
    try:
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.show()
    except Exception as e:
        print(f"Error occurred while plotting scatter plot: {str(e)}")

def sendDataToWB(mae: np.ndarray, mse: np.ndarray, rmse: np.ndarray, params_model) -> None:
    wb.init(
      # Set the project where this run will be logged
      project=params_model.get("project_name", "PJA-ASI-12C-GR1"),
      )
    wb.log({"mae": mae, "mse": mse, "rmse": rmse})
    wb.finish()