import pandas as pd
import logging
from typing import Callable
from utils.exceptions import EmptyData

logger = logging.getLogger('database')


def try_to_load_data(data_load_function: Callable) -> pd.DataFrame:
    def wrap():
        try:
            df = data_load_function()
        except Exception:
            raise

        if df.empty:
            raise EmptyData(f'{data_load_function.__name__} empty result.')

        return df
    return wrap


@try_to_load_data
def get_bills_data() -> pd.DataFrame:
    return pd.read_csv('csvs/bills.csv')


@try_to_load_data
def get_legislators_data() -> pd.DataFrame:
    return pd.read_csv('csvs/legislators.csv')


@try_to_load_data
def get_votes_data() -> pd.DataFrame:
    return pd.read_csv('csvs/votes.csv')


@try_to_load_data
def get_vote_results_data() -> pd.DataFrame:
    return pd.read_csv('csvs/vote_results.csv')