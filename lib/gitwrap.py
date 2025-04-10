# Import dependencies
from github import Github, Auth
from github.Repository import Repository
from github.ContentFile import ContentFile
from github.NamedUser import NamedUser as User
from github.AuthenticatedUser import AuthenticatedUser as AuthUser
from time import sleep
import logging
log = logging.getLogger(__name__)

# Import libraries
from lib import github_error_handle
from config import Config


class GitWrap:  # Like giftwrap? Ehh? :)
    def __init__(self, token):
        # Singleton Config
        self.config = Config()
        # Github caches
        self._user: User | AuthUser | None = None
        self._repos: list[Repository] | None = None
        self._readmes: list[ContentFile] | None = None
        # Creating instance with error wrapper
        self.create_github_instance(token)

    @github_error_handle
    def create_github_instance(self, token):
        auth = Auth.Token(token)
        self.gh: Github = Github(auth = auth)
        return self

    @property
    @github_error_handle
    def personal_info(self) -> User | AuthUser:
        if self._user is None:
            self._user = self.gh.get_user()
            self._user._completeIfNeeded()
            log.debug(f'Fetched and cached user\'s info.')
        return self._user

    @property
    @github_error_handle
    def repos(self) -> list[Repository]:
        if self._repos is None:
            self.personal_info  # Calls attribute-method to ensure existence
            self._repos = list(self._user.get_repos())
            log.debug('Fetched and cached user\'s repo data.')
        return self._repos

    @property
    @github_error_handle
    def readmes(self) -> list[ContentFile]:
        if self._readmes is None:
            self.repos  # Calls attribute-method to ensure existence
            self._readmes = []
            for repo in self._repos:
                self._readmes.append(repo.get_readme())
                sleep(self.config.SLEEP)
            log.debug('Fetched and cached user\'s READMEs.')
        return self._readmes
    
    def clear_cache(self, cache: str | None = None) -> None:
        '''Clears the cached user, repos, and readmes.

        If a specific cache is provided via the 'cache' parameter, only that cache will be cleared.
        Otherwise, all caches are cleared.

        Args:
            cache (str | None): The specific cache to clear. Acceptable values are "user", "repos", or "readmes". If None (default), all caches are cleared.'''
        if cache is None:
            self._user = None
            self._repos = None
            self._readmes = None
            log.debug('Cleared all GitWrap caches.')
        elif cache == 'user':
            self._user = None
            log.debug('Cleared GitWrap user cache.')
        elif cache == 'repos':
            self._repos = None
            log.debug('Cleared GitWrap repos cache.')
        elif cache == 'readmes':
            self._readmes = None
            log.debug('Cleared GitWrap readmes cache.')
        else:
            log.warning('Invalid cache key specified: "%s". No caches were cleared.', cache)
        return None


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')