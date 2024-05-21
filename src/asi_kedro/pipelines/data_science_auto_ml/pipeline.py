"""
This is a boilerplate pipeline 'explicit_or_autogluon'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data, train_model_auto_ml, sendDataToWB


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["studentData", "params:data_split"],
            outputs=["fullSet_train_validate", "fullSet_test"],
            name="train_test_split_autoML"
        ),
        node(
            func=split_data,
            inputs=["fullSet_train_validate", "params:data_split"],
            outputs=["fullSet_train", "fullSet_validate"],
            name="train_validate_split_autoML"
        ),
        node(
            func=train_model_auto_ml,
            inputs=["fullSet_train", "fullSet_validate", "params:auto_ml_config"],
            outputs="challenger",
            name="train_model_autoML"
        ),
        node(
            func=sendDataToWB,
            inputs=["results_challenger", "params:model_autoML"],
            name="send_to_Weights_and_Biases_autoML",
            outputs=None
        )
    ])