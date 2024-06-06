"""
This is a boilerplate pipeline 'data_deployment_2'
generated using Kedro 0.19.3
"""
import os, shutil
import pickle
from types import NoneType
import pandas as pd
from typing import Tuple, Union
from typing import Any
from autogluon.tabular import TabularPredictor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# def load_champion_model() -> Union[TabularPredictor, LinearRegression, str]:
#     models_path = "data//06_models//champion"
#     champion_model_path = os.path.join(models_path, "predictor.pkl")
#     if os.path.isfile(champion_model_path):
#         with open(champion_model_path, 'rb') as file:
#             champion_model = pickle.load(file)
#         return champion_model
#     else:
#         return ""

def load_champion_model() -> Union[TabularPredictor, LinearRegression, str]:
    models_path = "data//06_models//champion"
    predictor_path = os.path.join(models_path, "predictor.pkl")
    raw_path = os.path.join(models_path, "model.pkl")
    if os.path.isfile(predictor_path):
        champion_predictor = TabularPredictor.load("data/06_models/champion")
        return champion_predictor
    elif os.path.isfile(raw_path):
        with open(raw_path, 'rb') as file:
            champion_model = pickle.load(file)
            return champion_model
    else:
        return ""

def delete_defeated_champion():
    folder = "data//06_models//champion"
    if os.path.exists("data//06_models//champion"):
        shutil.rmtree(folder)
def delete_challenger():
    folder = "data//06_models//challenger"
    if os.path.exists("data//06_models//challenger"):
        shutil.rmtree(folder)

def turn_challenger_into_champion(challenger):
    if isinstance(challenger, TabularPredictor):
        challenger.clone("data//06_models//champion")
    if isinstance(challenger, LinearRegression):
        shutil.copytree("data//06_models//challenger", "data//06_models//champion") 

def evaluate_model(challenger: TabularPredictor | LinearRegression, champion: TabularPredictor | LinearRegression, data_test: pd.DataFrame, params_auto_ml) -> Tuple[TabularPredictor | LinearRegression]:
    # try:
        winner = {}
        r2_champion = None
        r2_challenger = None
        print(champion)
        if champion:
            if isinstance(champion, TabularPredictor):
                print('Champion is a TabularPredictor')
                r2_champion = -champion.evaluate(data_test)['root_mean_squared_error']
            
            if isinstance(champion, LinearRegression):
                print('Champion is a LinearRegression')
                x_test = data_test.drop(columns=[params_auto_ml.get('label_column', 'math_score')], inplace=False)
                y_test = data_test[params_auto_ml.get('label_column', 'math_score')]
                champion_results = champion.predict(x_test)
                r2_champion = r2_score(y_test, champion_results)

            if isinstance(challenger, TabularPredictor):
                print('Challenger is a TabularPredictor')
                r2_challenger = -challenger.evaluate(data_test)['root_mean_squared_error']
            
            if isinstance(challenger, LinearRegression):
                print('Challenger is a LinearRegression')
                x_test = data_test.drop(columns=[params_auto_ml.get('label_column', 'math_score')], inplace=False)
                y_test = data_test[params_auto_ml.get('label_column', 'math_score')]
                challenger_results = challenger.predict(x_test)
                r2_challenger = r2_score(y_test, challenger_results)

            print(f'Champion r2: {r2_champion}')
            print(f'Challenger r2: {r2_challenger}')
            if r2_champion > r2_challenger :
                winner = challenger
                print('Challenger won!')
                delete_defeated_champion()
                turn_challenger_into_champion(challenger)
            else:
                winner = champion
                print('Champion is undefeated!')
        else:
            winner = challenger
            print('Challenger is the first model')
            delete_defeated_champion()
            turn_challenger_into_champion(challenger)

        delete_challenger()
        return winner

    # except Exception as e:
    #     print(f"Error occurred while evaluating the model: {str(e)}")
    #     return None