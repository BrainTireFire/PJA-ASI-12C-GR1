"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, evaluate_model, sendDataToWB, separate_dependent_variable, preprocess_data, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=separate_dependent_variable,
            inputs="studentData",
            outputs=["X","Y"],
            name="separate_dependent_variable"
        ),
        node(
            func=preprocess_data,
            inputs="X",
            outputs="X_processed",
            name="preprocess_data"
        ),
        node(
            func=split_data,
            inputs=["X_processed", "Y", "params:data_split"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="train_test_split"
        ),
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
