import pandas as pd
import logging
from typing import Dict

logger = logging.getLogger('report_legislators_support_oppose_count')


def generate_legislators_support_oppose_count(
        databases: Dict[str, pd.DataFrame],
) -> None:
    merged_df = merge_generate_legislators_support_oppose_count(
        vote_results_df = databases['vote_results_df'],
        votes_df = databases['votes_df'],
        legislators_df = databases['legislators_df'],
    )
    aggregated_df = aggregate_generate_legislators_support_oppose_count(merged_df)
    aggregated_df.to_csv('outputs/legislators-support-oppose-count.csv')


def merge_generate_legislators_support_oppose_count(
    vote_results_df : pd.DataFrame,
    votes_df : pd.DataFrame,
    legislators_df : pd.DataFrame,
) -> pd.DataFrame:
    pass


def aggregate_generate_legislators_support_oppose_count(
    merged_df : pd.DataFrame,
) -> pd.DataFrame:
    pass
