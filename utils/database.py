import pandas as pd
import logging
from typing import Callable
from utils.exceptions import EmptyData

logger = logging.getLogger('database')


def try_to_load_data(data_load_function: Callable) -> pd.DataFrame:
    def wrap():
        df = data_load_function()
        if df.empty:
            raise EmptyData(f'{data_load_function.__name__} empty result.')
    return wrap

@try_to_load_data
def get_bills_data() -> pd.DataFrame:
    pass

@try_to_load_data
def get_legislators_data() -> pd.DataFrame:
    pass

@try_to_load_data
def get_votes_data() -> pd.DataFrame:
    pass

@try_to_load_data
def get_vote_results_data() -> pd.DataFrame:
    pass