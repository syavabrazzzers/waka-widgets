from os import environ

from gh import GitHubManager
from readme_editor import ReadmeEditor
from waka import Wakatime


if __name__ == '__main__':
    print(environ)
    waka = Wakatime(environ['INPUT_WAKATIME_API_KEY'])
    editors = waka.user_stats()
    zxc = GitHubManager(token=environ['INPUT_GH_TOKEN'])
    data = ReadmeEditor(zxc, waka)
    data.generate_data()
    # data.save_changes()
    # zxc.commit()

