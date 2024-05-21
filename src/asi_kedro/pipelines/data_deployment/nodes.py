"""
This is a boilerplate pipeline 'data_deployment'
generated using Kedro 0.19.3
"""

import pandas as pd
from typing import Tuple
from typing import Any
from autogluon.tabular import TabularPredictor

def evaluate_model_auto_ml(challenger: TabularPredictor, champion: TabularPredictor, test_data: pd.DataFrame, params_auto_ml) -> Tuple[Any, TabularPredictor]:
    try:
        if(challenger is champion):
            print('ten sam obiekt')
        print(hash(challenger))
        print(hash(champion))
        winner = {}
        results_challenger = challenger.evaluate(test_data)
        results_champion = champion.evaluate(test_data)
        print(results_challenger)
        print(results_champion)
        if(results_challenger['root_mean_squared_error'] > results_champion['root_mean_squared_error']):
            print('New champion!')
            winner = challenger
        else:
            print('Challenger failed to best the champion')
            winner = champion
        # print(predictor.leaderboard(test_data, silent=True))
        return results_challenger, winner
    except Exception as e:
        print(f"Error occurred while evaluating the model: {str(e)}")
        return None, None