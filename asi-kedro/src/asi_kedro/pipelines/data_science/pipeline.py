"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, evaluate_model, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["X_processed", "Y"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="train_test_split"
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs="model",
            name="training_model"
        ),
        node(
            func=evaluate_model,
            inputs=["model", "y_test", "X_test"],
            outputs=["mae", "rmse", "r2_square"],
            name="evaluate_model"
        )])
