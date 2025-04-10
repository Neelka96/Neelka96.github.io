from lib import Database

def load_languages():
    with Database().get_session() as session:
        session


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')