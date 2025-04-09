if __name__ == '__main__':
    # Setup logger before any imports begin
    from core.logger import log_setup
    log_setup()

    # Dependencies
    from core.gitwrap import GitWrap
    from Config import Config
    import logging
    
    
    log = logging.getLogger(__name__)
    config = Config()
    gh = GitWrap(config.GIT_TOKEN)
    gh.readmes