import pandas as pd
import logging
from typing import Dict
from utils.database import VOTE_LABELS_DICT
from utils.exceptions import InconsistentData

logger = logging.getLogger('report_bills_support_oppose_count_with_main_sponsor')

def generate_bills_support_oppose_count_with_main_sponsor(
        databases: Dict[str, pd.DataFrame],
) -> None:
    logger.info('function generate_legislators_support_oppose_count initiated')
    merged_df = merge_generate_bills_support_oppose_count_with_main_sponsor(
        vote_results_df = databases['vote_results_df'],
        votes_df = databases['votes_df'],
        legislators_df = databases['legislators_df'],
        bills_df = databases['bills_df'],
    )

    # Making sure that we aren't duplicating or removing votes by accident.
    if len(databases['vote_results_df']) != len(merged_df):
        raise InconsistentData('Votes duplicated or deleted by error. Check implementation.')

    logger.info('Data consistency check passed')

    aggregated_df = aggregate_generate_bills_support_oppose_count_with_main_sponsor(merged_df)
    aggregated_df.to_csv('outputs/bills-support-oppose-count-with-main-sponsor.csv')


def merge_generate_bills_support_oppose_count_with_main_sponsor(
    vote_results_df : pd.DataFrame,
    votes_df : pd.DataFrame,
    legislators_df : pd.DataFrame,
    bills_df : pd.DataFrame,
) -> pd.DataFrame:
    logger.info('function merge_generate_bills_support_oppose_count_with_main_sponsor initiated')

    merged_df = pd.merge(vote_results_df, votes_df, how='left', left_on='vote_id', right_on='id')

    merged_df = pd.merge(merged_df, bills_df, how='left', left_on='bill_id', right_on='id')
    merged_df = merged_df.rename(columns={'title' : 'bill_name'})

    merged_df = pd.merge(merged_df, legislators_df, how='left', left_on='sponsor_id', right_on='id')
    merged_df = merged_df.rename(columns={'name' : 'sponsor_name'})

    merged_df['sponsor_name'] = merged_df['sponsor_name'].fillna('No Sponsor')

    merged_df = merged_df[['bill_name', 'sponsor_name', 'legislator_id', 'vote_type']]

    merged_df['vote_type'] = merged_df['vote_type'].replace(VOTE_LABELS_DICT)

    return merged_df



def aggregate_generate_bills_support_oppose_count_with_main_sponsor(
    merged_df : pd.DataFrame,
) -> pd.DataFrame:
    logger.info('function aggregate_generate_bills_support_oppose_count_with_main_sponsor initiated')
    return merged_df.pivot_table(index=['bill_name', 'sponsor_name'], columns='vote_type', values='legislator_id', aggfunc='count')
