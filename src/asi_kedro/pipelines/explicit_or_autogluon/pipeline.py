"""
This is a boilerplate pipeline 'explicit_or_autogluon'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["studentData", "params:data_split"],
            outputs=["fullSet_train", "fullSet_test"],
            name="train_test_split2"
        )
    ])
