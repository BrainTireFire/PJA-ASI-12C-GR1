"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def split_data(X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X: np.ndarray, y: np.ndarray) -> Tuple[LinearRegression]:
    try:
        model = LinearRegression(fit_intercept=True)
        model.fit(X, y)
        return model
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None


def evaluate_model(model: LinearRegression, true: np.ndarray, X_test: np.ndarray) -> Tuple[float, float, float]:
    try:
        predicted = model.predict(X_test)
        mae = mean_absolute_error(true, predicted)
        mse = mean_squared_error(true, predicted)
        rmse = np.sqrt(mse)
        r2_square = r2_score(true, predicted)
        return mae, rmse, r2_square
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None, None, None

def plot_scatter(y_test: np.ndarray, y_pred: np.ndarray) -> None:
    try:
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.show()
    except Exception as e:
        print(f"Error occurred while plotting scatter plot: {str(e)}")