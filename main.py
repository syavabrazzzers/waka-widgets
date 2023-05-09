from os import environ

from gh import GitHubManager
from readme_editor import ReadmeEditor
from waka import Wakatime


if __name__ == '__main__':
    waka = Wakatime(environ['INPUT_WAKATIME_API_KEY'])
    editors = waka.user_stats()
    github = GitHubManager(token=environ['INPUT_GH_TOKEN'])
    data = ReadmeEditor(github, waka)
    data.generate_data()
    data.save_changes()
    github.commit()

