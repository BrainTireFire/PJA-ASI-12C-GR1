"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from kedro.config import OmegaConfigLoader
from kedro.framework.project import settings
from pathlib import Path

import asi_kedro.pipelines.data_processing as dp
import asi_kedro.pipelines.data_science_automl as ds_automl
import asi_kedro.pipelines.data_science_linearreg as ds_LinearRegression
import asi_kedro.pipelines.model_deployment as ds_champion_challenger

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    # Find and register pipelines
    pipelines = find_pipelines()
    

    data_processing_pipeline = dp.create_pipeline()
    data_science_automl_pipeline = ds_automl.create_pipeline()
    data_science_LinReg_pipeline = ds_LinearRegression.create_pipeline()
    ds_champion_challenger_pipeline = ds_champion_challenger.create_pipeline()

    return {
        "automl": data_processing_pipeline + data_science_automl_pipeline + ds_champion_challenger_pipeline,
        "LinReg": data_processing_pipeline + data_science_LinReg_pipeline + ds_champion_challenger_pipeline,
    }
