from functools import wraps
from github import (
    GithubException
    ,BadCredentialsException
    ,BadAttributeException
    ,RateLimitExceededException
    ,BadUserAgentException
    ,UnknownObjectException
    ,TwoFactorException
    )

import logging
log = logging.getLogger(__name__)

def github_error_handle(func):
    '''Error handler for all Github API issues.

    Args:
        func (Callable): Github API method being wrapped.

    Yields:
        Generator
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadCredentialsException as e:
            log.exception('Invalid credentials provided to GitHub!')
            raise
        except BadAttributeException as e:
            log.exception('Wrong attribute type returned by GitHub!')
            raise
        except RateLimitExceededException as e:
            log.exception('GitHub rate limit exceeded!')
            raise
        except BadUserAgentException as e:
            log.exception('GitHub request sent with bad user agent header.')
            raise
        except UnknownObjectException as e:
            log.exception('GitHub request for non-existent object.')
            raise
        except TwoFactorException as e:
            log.exception('GitHub onetime password for two-factor authentication required.')
            raise
        except GithubException as e:
            log.exception(f'GitHub API error (status {e.status}): {e.data}')
            raise RuntimeError(f'GitHub API error: {e.status}') from e

    return wrapper


# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')