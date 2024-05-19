"""
This is a boilerplate pipeline 'explicit_or_autogluon'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data, train_model_auto_ml, evaluate_model_auto_ml


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["studentData", "params:data_split"],
            outputs=["fullSet_train_validate", "fullSet_test"],
            name="train_test_split2"
        ),
        node(
            func=split_data,
            inputs=["fullSet_train_validate", "params:data_split"],
            outputs=["fullSet_train", "fullSet_validate"],
            name="train_validate_split"
        ),
        node(
            func=train_model_auto_ml,
            inputs=["fullSet_train", "fullSet_validate", "params:auto_ml_config"],
            outputs="predictor_MR",
            name="train_model_auto_ml_MR"
        ),
        node(
            func=evaluate_model_auto_ml,
            inputs=["predictor_MR", "fullSet_test", "params:auto_ml_config"],
            outputs="results_MR",
            name="evaluate_model_auto_ml_MR"
        )
    ])