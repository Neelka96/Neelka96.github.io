if __name__ == '__main__':
    # Setup logger before any imports begin
    from core.logger import log_setup
    log_setup()

    # Dependencies
    from core.GitWrap import GitWrap
    from Config import Config
    from pprint import pprint
    from dotenv import load_dotenv
    import logging
    
    
    log = logging.getLogger(__name__)
    load_dotenv()
    config = Config()
    gh = GitWrap(config.GIT_TOKEN)
    gh.readmes