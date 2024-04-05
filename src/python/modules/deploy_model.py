from joblib import dump
import os

def save_model(model, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    dump(model, os.path.join(output_dir, 'model.joblib'))