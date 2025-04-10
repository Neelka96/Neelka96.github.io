import logging
log = logging.getLogger(__name__)

from .extract import get_github_languages
from .transform import get_language_names
from config import Config
config = Config()


class Linguist_Pipeline:
    def __init__(self):
        self.data = self.extraction()
        self.names = self.transformation()
        self.loading()
    
    def extraction(self):
        self.data = get_github_languages(config.LINGUIST_URL, config.LINGUIST_CACHE)
        return self.data
    
    def transformation(self):
        self.names = get_language_names(self.data)
        return self.names
    
    def loading(self):
        ...
    
    def __repr__(self):
        rows = len(self.data)
        cols = len(list(self.data.values())[0])
        return f'<LinguistPipeline(rows={rows}, cols={cols})>'
    
    def __iter__(self):
        for key, value in self.data.items():
            yield (key, value)


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')