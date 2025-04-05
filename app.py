from pprint import pprint
if __name__ == '__main__':
    # Setup logger before any imports begin
    from core.logger import log_setup
    log_setup()

    # Dependencies
    from core.GitWrap import GitWrap
    from config.settings import get_settings
    from dotenv import load_dotenv
    # from pprint import pprint
    import logging

    log = logging.getLogger(__name__)
    load_dotenv()
    config = get_settings()
    gh = GitWrap(config.get('GIT_TOKEN'))

    for r in gh.get_repo_data:
        print(r)