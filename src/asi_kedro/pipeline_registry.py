"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from kedro.config import OmegaConfigLoader
from kedro.framework.project import settings

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    # conf_path = str(project_path / settings.CONF_SOURCE)
    # conf_loader = OmegaConfigLoader(conf_source=conf_path)
    # automl_enabled = conf_loader["automl"]
    automl_enabled = False

    # Find and register pipelines
    pipelines = find_pipelines()
    
    if automl_enabled:
        pipelines["__default__"] = pipelines.get("data_processing", Pipeline([])) + pipelines.get("data_science_auto_ml", Pipeline([])) + pipelines.get("data_deployment", Pipeline([]))
    else:
        pipelines["__default__"] = pipelines.get("data_processing", Pipeline([])) + pipelines.get("data_science", Pipeline([]))

    return pipelines
