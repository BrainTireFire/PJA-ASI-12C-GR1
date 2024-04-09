"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node
from .nodes import plot_scatter, evaluate_model, train_model, save_model

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            plot_scatter,
            inputs={"y_test": "y_test", "y_pred": "y_pred"},
            outputs=None
        ),
        node(
            evaluate_model,
            inputs={"true": "true", "predicted": "predicted"},
            outputs=["mae", "rmse", "r2_square"]
        ),
        node(
            train_model,
            inputs={"X": "X", "y": "y"},
            outputs=["model", "X_test", "y_test"]
        ),
        node(
            save_model,
            inputs={"model": "model", "output_dir": "output_dir"},
            outputs=None
        )
    ])
