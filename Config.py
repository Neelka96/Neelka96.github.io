import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load()
        return cls._instance
    
    def _load(self):
        self.ENV = os.environ.get('APP_ENV', 'development').lower()
        self.GIT_TOKEN = os.environ.get('GIT_TOKEN')
        self.AZURE_CONN = os.environ.get('AZURE_CONN')
        self.STORAGE_ACCT_CONN = os.environ.get('STORAGE_ACCT_CONN')
        self.STORAGE = os.environ.get('STORAGE', '/resources')
        self.LOG_LEVEL = self.__get_log_level()
        self.LOG_FILE = os.environ.get('LOG_FILE', 'app.log')
        self.SLEEP = 0.5
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