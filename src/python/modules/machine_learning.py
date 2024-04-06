from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from typing import Tuple

def train_model(X: np.ndarray, y: np.ndarray) -> Tuple[LinearRegression, np.ndarray, np.ndarray]:
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression(fit_intercept=True)
        model.fit(X_train, y_train)
        return model, X_test, y_test
    except Exception as e:
        print(f"Error occurred while training the model: {str(e)}")
        return None, None, None