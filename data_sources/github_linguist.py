import requests
import yaml
import logging
log = logging.getLogger(__name__)

from Config import Config
config = Config()


def fetch_github_linguist() -> dict:
    # Assign variables from config
    url = config.LINGUIST_URL
    cache = config.LINGUIST_CACHE

    # Check for cache/file existence -> Load it exit early
    if cache.exists():
        log.debug('Reading github-linguist YAML from cache.')
        return yaml.safe_load(cache.read_text())
    
    # To a full requests and then load it into the cache
    log.debug('Making a full request for github-linguist YAML.')
    response = requests.get(url)
    response.raise_for_status()
    data = yaml.safe_load(response.text)

    log.debug('Writing YAML data to cache.')
    cache.write_text(yaml.dump(data))
    
    return data