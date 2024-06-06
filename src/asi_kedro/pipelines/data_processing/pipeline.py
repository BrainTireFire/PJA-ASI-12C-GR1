"""
This is a boilerplate pipeline 'data_processing_2'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import preprocess_data, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_data,
            inputs="studentData",
            outputs=["studentData_preprocessed", "numeric_transformer", "label_encoders"],
            name="preprocess_data"
        ),
        node(
            func=split_data,
            inputs=["studentData_preprocessed", "params:data_split"],
            outputs=["data_train", "data_test"],
            name="split_data"
        ),
    ]);
