import pandas as pd
import logging
from typing import Dict

logger = logging.getLogger('report_bills_support_oppose_count_with_main_sponsor')

def generate_bills_support_oppose_count_with_main_sponsor(
        databases: Dict[str, pd.DataFrame],
) -> None:
    merged_df = merge_generate_bills_support_oppose_count_with_main_sponsor(
        vote_results_df = databases['vote_results_df'],
        votes_df = databases['votes_df'],
        legislators_df = databases['legislators_df'],
        bills_df = databases['bills_df'],
    )
    aggregated_df = aggregate_generate_bills_support_oppose_count_with_main_sponsor(merged_df)
    aggregated_df.to_csv('outputs/bills-support-oppose-count-with-main-sponsor.csv')

def merge_generate_bills_support_oppose_count_with_main_sponsor(
    vote_results_df : pd.DataFrame,
    votes_df : pd.DataFrame,
    legislators_df : pd.DataFrame,
    bills_df : pd.DataFrame,
) -> pd.DataFrame:
    pass


def aggregate_generate_bills_support_oppose_count_with_main_sponsor(
    merged_df : pd.DataFrame,
) -> pd.DataFrame:
    pass
