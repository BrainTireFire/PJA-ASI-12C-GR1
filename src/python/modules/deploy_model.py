from joblib import dump
import os
from typing import Any

def save_model(model: Any, output_dir: str) -> None:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        dump(model, os.path.join(output_dir, 'model.joblib'))
        print("Model saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving the model: {str(e)}")