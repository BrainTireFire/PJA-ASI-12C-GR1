"""
This is a boilerplate pipeline 'data_science_2'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model_auto_ml, sendDataToWB, evaluate


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model_auto_ml,
            inputs=["data_train", "params:auto_ml_config"],
            outputs="challenger",
            name="train_model_auto_ml"
        ),
        node(
            func=evaluate,
            inputs=["challenger", "data_test"],
            outputs="results_challenger",
            name="evaluate"
        ),
        node(
            func=sendDataToWB,
            inputs=["results_challenger", "params:model"],
            outputs=None,
            name="sendDataToWB"
        ),
    ]);
