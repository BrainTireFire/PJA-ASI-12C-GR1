"""
This is a boilerplate pipeline 'data_deployment_2'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_model, load_champion_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_champion_model,
            inputs=None,
            outputs="champion",
            name="load_champion_model"
        ),
        node(
            func=evaluate_model,
            inputs=["challenger", "champion", "data_test", "params:auto_ml_config"],
            outputs="winner",
            name="evaluate_model_autoML"
        ),
    ])
