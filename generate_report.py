import logging
from utils.database import get_bills_data, get_legislators_data, get_vote_results_data, get_votes_data
from utils.report_legislators_support_oppose_count import generate_legislators_support_oppose_count
from utils.report_bills_support_oppose_count_with_main_sponsor import generate_bills_support_oppose_count_with_main_sponsor
from utils.exceptions import EmptyData, InconsistentData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s [%(levelname)s] %(message)s')

logger = logging.getLogger('main')

def main():
    logger.info('Loading data. ')

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
    
    logger.info('Data loaded successfully.')
    # future feature: Check if folder "outputs" exists and create if it doens't.
    try:
        generate_legislators_support_oppose_count(databases)
        generate_bills_support_oppose_count_with_main_sponsor(databases)

    except InconsistentData as e:
        logger.error(e)
        return

    except Exception as e:
        logger.error(f'Error generating report data: {e}')
        return

main()