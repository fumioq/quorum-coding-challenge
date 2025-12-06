import pandas as pd
import logging
from typing import Dict
from utils.database import get_bills_data, get_legislators_data, get_vote_results_data, get_votes_data
from utils.reports import generate_bills_support_oppose_count_with_main_sponsor, generate_legislators_support_oppose_count
from utils.exceptions import EmptyData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s [%(levelname)s] %(message)s')

logger = logging.getLogger('main')

def main():
    try:
        databases = {
            "bills_df" : get_bills_data(),
            "legislators_df" : get_legislators_data(),
            "votes_df" : get_votes_data(),
            "vote_results_df" : get_vote_results_data(),
        }
    except EmptyData as e:
        logger.error(e)
        return

    except Exception as e:
        logger.error(f'Error loading data: {e}')
        return

    generate_legislators_support_oppose_count(databases)
    generate_bills_support_oppose_count_with_main_sponsor(databases)

if __name__ == "__generate_report__":
    main()