from collections.abc import Sequence
from sqlalchemy import insert

from lib import Database
db = Database()

def load_languages(lang_obj: Sequence[dict]):
    stmt = insert(lang_obj)
    db.execute_query(stmt)

# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')