from pathlib import Path
import requests
import yaml
import logging
log = logging.getLogger(__name__)


def get_github_languages(url: str, cache: Path) -> dict:
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


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')