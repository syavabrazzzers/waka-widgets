from os import getenv
from os.path import join

from gh import GitHubManager
from readme_editor import ReadmeEditor
from waka import Wakatime
from git import Repo
from github import Github, Repository


if __name__ == '__main__':
    waka = Wakatime('waka_d7df8f9f-c811-4940-a658-74b38f5c31e1')
    editors = waka.user_stats()
    zxc = GitHubManager(token='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')
    data = ReadmeEditor(zxc, waka)
    data.generate_data()
    data.save_changes()
    zxc.commit()
    # print(data.get_content())
    # with open("repo/README.md", "a") as myfile:
    #     myfile.write("appended text")
    # zxc.commit()
    # print(editors['data'])

