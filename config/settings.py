import os

# class EnvVars:
#     def __init__(self):
#         self.ENV = os.environ.get('APP_ENV', 'development')
#         self.LOG_LEVEL = os.environ.get(
#                 'LOG_LEVEL', 'DEBUG' 
#                 if os.environ.get('APP_ENV') == 'development' 
#                 else 'INFO'
#             )


def get_settings():
    return \
        {
            'ENV': os.environ.get('APP_ENV', 'development')
            ,'GIT_TOKEN': os.environ.get('GIT_TOKEN')
            ,'AZURE_CONN': os.environ.get('AZURE_CONN')
            ,'STORAGE_ACCT_CONN': os.environ.get('STORAGE_ACCT_CONN')
            ,'STORAGE': os.environ.get('STORAGE', '/resources')
            ,'LOG_LEVEL': os.environ.get(
                'LOG_LEVEL', 'DEBUG' 
                if os.environ.get('APP_ENV') == 'development' 
                else 'INFO'
            )
            ,'LOG_FILE': os.environ.get('LOG_FILE', 'app.log')
        }