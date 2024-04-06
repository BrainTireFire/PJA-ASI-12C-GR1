from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

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