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
            cls._instance._engine_meta()
        return cls._instance
    
    def _load_env_vars(self):
        self.ENV = os.environ.get('APP_ENV', 'development').lower()
        self.GIT_TOKEN = os.environ.get('GIT_TOKEN')
        self.AZURE_CONN = os.environ.get('AZURE_CONN')
        self.STORAGE_ACCT_CONN = os.environ.get('STORAGE_ACCT_CONN')
        self.STORAGE = Path(os.environ.get('STORAGE', '/resources'))
        self.LOG_LEVEL = self.__get_log_level()
        self.LOG_FILE = os.environ.get('LOG_FILE', 'app.log')
        self.SLEEP = os.environ.get('SLEEP', 1)
        return self
    
    def _engine_meta(self):
        self.__get_db_name()
        self.ENGINE_PATH = self.STORAGE / self.db_name
        self.ENGINE_URI = f'sqlite:///{self.ENGINE_PATH}'
        return self
    
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


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')