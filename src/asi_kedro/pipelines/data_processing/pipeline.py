"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import separate_dependent_variable, preprocess_data, split_data


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
    ])
