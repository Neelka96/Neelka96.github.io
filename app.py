from gh import GitWrap
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
GIT_TOKEN = os.environ.get('GIT_TOKEN', None)

git_api = GitWrap(GIT_TOKEN)

pprint(git_api.repos_data)