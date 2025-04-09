import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_env_vars()
            cls._instance._load_engine()
            cls._instance._get_github_linguist()
        return cls._instance
    
    def _load_env_vars(self):
        self.ENV = os.environ.get('APP_ENV', 'development').lower()
        self.GIT_TOKEN = os.environ.get('GIT_TOKEN')
        self.AZURE_CONN = os.environ.get('AZURE_CONN')
        self.STORAGE_ACCT_CONN = os.environ.get('STORAGE_ACCT_CONN')
        self.STORAGE = Path(os.environ.get('STORAGE', 'resources'))
        self.LOG_LEVEL = self.__get_log_level()
        self.LOG_FILE = os.environ.get('LOG_FILE', 'app.log')
        self.SLEEP = os.environ.get('SLEEP', 1)
        self.__correct_paths()
        return self
    
    def _load_engine(self):
        self.__get_db_name()
        self.ENGINE_PATH = self.STORAGE / self.db_name
        self.ENGINE_URI = f'sqlite:///{self.ENGINE_PATH}'
        return self

    def _get_github_linguist(self):
        self.LINGUIST_URL = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'
        self.LINGUIST_CACHE = self.STORAGE / 'linguist_cache.yaml'


    def __get_db_name(self):
        if self.ENV == 'production':
            self.db_name = 'gitwrap.sqlite'
        else:
            self.db_name = 'gitwrap_dev.sqlite'
        return self
    
    def __get_log_level(self):
        return os.environ.get(
            'LOG_LEVEL', 'DEBUG' 
            if os.environ.get('APP_ENV') == 'development' 
            else 'INFO'
        )
    
    def __correct_paths(self):
        if self.ENV == 'production':
            pass
        else:
            repo_root = Path(__file__).resolve().parent
            self.STORAGE = repo_root / self.STORAGE
        return self

# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')