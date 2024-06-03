"""
This is a boilerplate pipeline 'data_deployment_2'
generated using Kedro 0.19.3
"""
import pandas as pd
from typing import Tuple
from typing import Any
from autogluon.tabular import TabularPredictor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def evaluate_model(challenger: TabularPredictor | LinearRegression, champion: TabularPredictor | LinearRegression, data_test: pd.DataFrame, params_auto_ml) -> Tuple[TabularPredictor | LinearRegression]:
    try:
        winner = {}
        r2_champion = None
        r2_challenger = None

        if not champion:
            print('Champion is None')
            return challenger

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
        else:
            winner = champion
            print('Champion is undefeated!')

        return winner

    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None