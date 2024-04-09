"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node
from .nodes import clean_data, preprocess_data, download_dataset

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            download_dataset,
            inputs={"url": "url", "destination": "destination"},
            outputs=None
        ),
        node(
            clean_data,
            inputs="study_performance",
            outputs=["X_processed", "y"]
        ),
        node(
            preprocess_data,
            inputs="X",
            outputs="X_processed"
        )
    ])
