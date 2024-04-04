import pandas as pd
from modules.preprocessData import preprocess_data

def clean_data(data_path):
    df = pd.read_csv(data_path)
    # Here cleaning steps can be added
    print('Data cleaning completed')
    X = df.drop(columns=['math_score'], axis=1)
    y = df['math_score']
    X_processed = preprocess_data(X)
    return X_processed, y