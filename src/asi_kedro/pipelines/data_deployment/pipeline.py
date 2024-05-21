"""
This is a boilerplate pipeline 'data_deployment'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_model_auto_ml

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
            node(
            func=evaluate_model_auto_ml,
            inputs=["challenger", "champion", "fullSet_test", "params:auto_ml_config"],
            outputs=["results_challenger", "winner"],
            name="evaluate_model_autoML"
        ),
    ])
