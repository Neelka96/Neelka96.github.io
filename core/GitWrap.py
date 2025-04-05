from github import Github, Auth
from github.Repository import Repository
from github.NamedUser import NamedUser as User
from github.AuthenticatedUser import AuthenticatedUser as AuthUser

import logging
log = logging.getLogger(__name__)

from .decorators import github_error_handle

class GitWrap:  # Like giftwrap? Ehh? :)
    def __init__(self, token):
        # API Caches
        self._user_cache: User | AuthUser | None = None
        self._repos_cache: list[Repository] | None = None

        # GitHub Setup
        auth = Auth.Token(token)
        self.gh: Github = Github(auth = auth)

    @property
    @github_error_handle
    def get_personal_info(self):
        if self._user_cache is None:
            self._user_cache = self.gh.get_user()
            log.debug('Fetched and cached user info.')
        return self._user_cache

    @property
    @github_error_handle
    def get_repo_data(self):
        if self._repos_cache is None:
            self._repos_cache = list(self.gh.get_user().get_repos())
            log.debug('Fetched and cached user\'s repo data.')
        return self._repos_cache