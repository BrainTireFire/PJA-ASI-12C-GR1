"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import separate_dependent_variable, preprocess_data


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
        )
    ])
