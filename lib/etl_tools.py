# Import dependencies
from collections.abc import Callable
import pandas as pd

# Personal dependencies
import logging
log = logging.getLogger(__name__)

from config import Config
config = Config()


def create_dict(
        translation: Callable[[int], str]
        ,ref_list: list[str]
        ) -> dict[str, str]:
    '''Used to create lightweight reference dictionaries for transformations.

    Args:
        translation (Callable[[int], str]): Function to map against constants.
        ref_list (list[str]): Constants used for mappings.

    Returns:
        dict[str, str]: Mapped dictionary with reference ids.
    '''
    log.debug('Creating dictionary for reference table.')
    # Dictionary comprehension used to apply function to each item as it's placed in dictionary
    return {item : translation(num) for num, item in enumerate(ref_list, start = 1)}


def create_ref_table(
        mapping: dict[str, str]
        ,target_col: str
    ) -> pd.DataFrame:
    '''Readies reference/parent table for SQL insertion.

    Args:
        mapping (dict[str, str]): Mapping from `create_dict()`.
        target_col (str): Primary key column to be created.

    Returns:
        pd.DataFrame: 2 column table with unique IDs.
    '''
    log.debug('Creating reference table.')
    # Adds 'id' to target column's name to create reference ID column
    new_col = f'{target_col}_id'

    # Initializes the dataframe using dictionary pairs for values
    return pd.DataFrame(
        {
            new_col: mapping.values(),
            target_col: mapping.keys()
        }
    )

# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')