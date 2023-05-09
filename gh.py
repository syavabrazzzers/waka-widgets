from shutil import rmtree

from git import Repo, Actor
from github import Github, Repository, AuthenticatedUser


class GitHubManager:
    repo: Repo
    user: AuthenticatedUser
    remote: Repository

    def __init__(self, token: str):
        self.github = Github(token)
        self.user = self.github.get_user()
        rmtree('repo', ignore_errors=True)
        self.repo = Repo.clone_from(f"https://{token}@github.com/{self.user.login}/{self.user.login}.git", 'repo')
        self.remote = self.github.get_repo(f'{self.user.login}/{self.user.login}')

    def commit(self):
        self.repo.index.add(self.remote.get_readme().path)
        self.repo.index.commit('Readme stats update', author=Actor(self.user.name, self.user.email), committer=Actor(self.user.name, self.user.email))
        self.repo.remote().push(force=True, refspec='main')

    def get_readme(self):
        readme = self.remote.get_readme()
        print(self.repo.re_envvars)
