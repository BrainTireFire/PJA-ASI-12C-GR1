"""
This is a boilerplate pipeline 'data_science_auto_ml'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model_auto_ml, evaluate_model_auto_ml


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model_auto_ml,
            inputs=["params:auto_ml_config"],
            outputs="predictor",
            name="train_model_auto_ml"
        ),
        node(
            func=evaluate_model_auto_ml,
            inputs=["predictor", "params:auto_ml_config"],
            outputs="results",
            name="evaluate_model_auto_ml"
        )
    ])
