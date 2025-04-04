from github import Github, Auth


class GitWrap:  # Like giftwrap? Ehh? :)
    def __init__(self, token):
        auth = Auth.Token(token)
        self.gh: Github = Github(auth = auth)   # Let linter object type
        self.personal_info()
        self.get_repo_data()

    def personal_info(self):
        self.name = self.gh.get_user().name
        self.email = self.gh.get_user().email
        self.loc = self.gh.get_user().location
        return self

    def get_repo_data(self):
    # id
    # size
    # language/languages_url (even better with lines)
    # topics
    # tags
    # name
    # homepage
    # contributors_url
    # deployments_url
    # ssh_url/html_url (remember to add .git to the end of html_url)
    # created_at/pushed_at
    # description
    # clone_url
    # NULLS: forks/forks_count/has_discussions/license/stargazers_count/watchers/watchers_count/subscribers_count/subscribers_url/topics/
    # .get_readme()
    # .get_artifacts() or .get_artifact (.size_in_bytes) --> "Workflow runs technically"
        self.repos_data = \
            [
                {
                    'name': r.name
                    ,'size': r.size
                    ,'desc': r.description
                    ,'language_url': r.languages_url
                    ,'topics': r.topics
                    ,'tags': r.tags_url # Update later to actual API request to get the tags when I put the tags in
                    ,'ssh_cloning': r.ssh_url
                    ,'https_cloning': f'{r.html_url}.git'
                    ,'created_at': r.created_at
                    ,'pushed_at': r.pushed_at
                }
                for r in self.gh.get_user().get_repos()
            ]
        return self