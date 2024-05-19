"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""
from sklearn.linear_model import LinearRegression
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score
import wandb as wb


import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from typing import Any


def separate_dependent_variable(study_performance: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    try:
        df = study_performance
        # Here cleaning steps can be added
        X = df.drop(columns=['math_score'], axis=1)
        y = df['math_score']
        return X, y
    except Exception as e:
        print(f"Error occurred while separating dependent variable: {str(e)}")
        return None, None

def preprocess_data(X: pd.DataFrame) -> Any:
    try:
        num_features = X.select_dtypes(exclude="object").columns
        cat_features = X.select_dtypes(include="object").columns

        numeric_transformer = StandardScaler()
        oh_transformer = OneHotEncoder()

        preprocessor = ColumnTransformer(
            [
                ("OneHotEncoder", oh_transformer, cat_features),
                ("StandardScaler", numeric_transformer, num_features),        
            ]
        )

        X_processed = preprocessor.fit_transform(X)
        # X_processed = pd.DataFrame(X_processed, index=X.index, columns=X.columns);
            
        return X_processed
    except Exception as e:
        print(f"Error occurred while preprocessing the data: {str(e)}")
        return None

def split_data(X: np.ndarray, y: np.ndarray, params_data_split) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    test_size = params_data_split['test_size']
    random_state = params_data_split["random_state"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

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

def sendDataToWB(mae: np.ndarray, mse: np.ndarray, r2_square: np.ndarray, params_model) -> None:
    wb.init(
      # Set the project where this run will be logged
      project=params_model.get("project_name", "PJA-ASI-12C-GR1"),
      )
    wb.log({"mae": mae, "mse": mse, "r2_square": r2_square})
    wb.finish()