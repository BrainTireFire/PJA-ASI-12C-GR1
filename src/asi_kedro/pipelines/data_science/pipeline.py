"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, evaluate_model, sendDataToWB


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model,
            inputs=["X_train", "y_train", "params:model"],
            outputs="model",
            name="training_model"
        ),
        node(
            func=evaluate_model,
            inputs=["model", "y_test", "X_test",  "params:model"],
            outputs=["mae", "rmse", "r2_square"],
            name="evaluate_model"
        ),
        node(
            func=sendDataToWB,
            inputs=["mae", "rmse", "r2_square", "params:model"],
            name="send_to_Weights_and_Biases",
            outputs=None
        )
        ])
