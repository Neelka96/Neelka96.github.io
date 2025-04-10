if __name__ == '__main__':
    # Setup logger before any imports begin
    from lib import log_setup
    log_setup()

    # Dependencies
    from jobs.gitwrap_pipeline.gitwrap import GitWrap
    from config import Config
    import logging
    
    
    log = logging.getLogger(__name__)
    config = Config()
    gh = GitWrap(config.GIT_TOKEN)
    gh.readmes