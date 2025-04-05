import logging
import logging.config
from config.settings import get_settings
from dotenv import load_dotenv

def log_setup() -> None:
    load_dotenv()
    config = get_settings()
    # env = config.get('ENV')
    azure_conn = config.get('AZURE_CONN')
    log_level = config.get('LOG_LEVEL')
    log_file = config.get('LOG_FILE')

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(name)s: %(levelname)s - %(message)s',
                'datefmt': '%m-%d-%y %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': log_level,
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'level': log_level,
                'filename': log_file,
            },
            # 'azure': {
            #     'class': 'opencensus.ext.azure.log_exporter.AzureLogHandler',
            #     'level': log_level,
            #     'connection_string': azure_conn,
            # },
        },
        'root': {
            # 'handlers': ['console', 'file', 'azure'],
            'handlers': ['console', 'file'],
            'level': log_level,
        },
    }

    logging.config.dictConfig(logging_config)
    return None