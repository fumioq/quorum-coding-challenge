import pandas as pd
import logging
from typing import Dict
from utils.database import VOTE_LABELS_DICT
from utils.exceptions import InconsistentData

logger = logging.getLogger('report_legislators_support_oppose_count')


def generate_legislators_support_oppose_count(
        databases: Dict[str, pd.DataFrame],
) -> None:
    logger.info('function generate_legislators_support_oppose_count initiated')
    merged_df = merge_generate_legislators_support_oppose_count(
        vote_results_df = databases['vote_results_df'],
        votes_df = databases['votes_df'],
        legislators_df = databases['legislators_df'],
    )

    # Making sure that we aren't duplicating or removing votes by accident.
    if len(databases['vote_results_df']) != len(merged_df):
        raise InconsistentData('Votes duplicated or deleted by error. Check implementation.')

    logger.info('Data consistency check passed')

    aggregated_df = aggregate_generate_legislators_support_oppose_count(merged_df)
    aggregated_df.to_csv('outputs/legislators-support-oppose-count.csv')


def merge_generate_legislators_support_oppose_count(
    vote_results_df : pd.DataFrame,
    votes_df : pd.DataFrame,
    legislators_df : pd.DataFrame,
) -> pd.DataFrame:
    logger.info('function merge_generate_legislators_support_oppose_count initiated')

    merged_df = pd.merge(vote_results_df, legislators_df, how='left', left_on='legislator_id', right_on='id')
    merged_df = merged_df.rename(columns={'name' : 'legislator_name'})
    merged_df = merged_df[['legislator_name', 'vote_type', 'vote_id']]

    merged_df = pd.merge(merged_df, votes_df, how='left', left_on='vote_id', right_on='id')
    merged_df = merged_df[['legislator_name', 'vote_type', 'bill_id']]

    merged_df['vote_type'] = merged_df['vote_type'].replace(VOTE_LABELS_DICT)

    return merged_df

def aggregate_generate_legislators_support_oppose_count(
    merged_df : pd.DataFrame,
) -> pd.DataFrame:
    logger.info('function aggregate_generate_legislators_support_oppose_count initiated')
    return merged_df.pivot_table(index='legislator_name', columns='vote_type', values='bill_id', aggfunc='count')
