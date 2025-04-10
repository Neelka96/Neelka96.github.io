# Import dependencies
from math import ceil
import logging
log = logging.getLogger(__name__)

from .extract import get_github_languages
from .transform import parse_language_names
# from .load import load_languages

from lib import create_dict, create_ref_table
from config import Config
config = Config()


class Linguist_Pipeline:
    def __init__(self):
        self.extraction().transformation().loading()
    
    def extraction(self):
        self.raw_data = get_github_languages(config.LINGUIST_URL, config.LINGUIST_CACHE)
        return self
    
    def transformation(self):
        self.names = parse_language_names(self.raw_data)
        return self
    
    def loading(self):
        pk_translation = lambda id: f'L{id}'
        column_label = 'name'
        self.table = create_ref_table(create_dict(pk_translation, self.names), column_label)

        return self
    
    def __repr__(self):
        rows = len(self.raw_data)
        cols_list: list[dict] = list(self.raw_data.values())
        max_col_len = 0
        for cols in cols_list:
            len_ = len(list(cols))
            if len_ > max_col_len:
                max_col_len = len_
        return f'<LinguistPipeline(rows={rows}, cols={max_col_len})>'
    
    def __iter__(self):
        for key, value in self.raw_data.items():
            yield (key, value)


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')