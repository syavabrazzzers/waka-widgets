import re
from datetime import timedelta
from math import floor
from os import environ, getenv
from gh import GitHubManager
from pathlib import Path

from waka import Wakatime


class ReadmeEditor:
    manager: GitHubManager
    wakatime: Wakatime

    def __init__(self, manager: GitHubManager, wakatime: Wakatime):
        self.manager = manager
        self.wakatime = wakatime
        self.blocks = getenv('INPUT_BLOCKS', 'languages').split(',')
        self.content = ''

    def asd(self):
        return self.blocks

    def generate_data(self):
        content = ''

        for j in self.blocks:
            try:
                data = self.wakatime.user_stats()['data'][j]
                content += f'## {" ".join(j.split("_")).capitalize()} used in the last week\n'
                content += '```text\n'
                for i in data:
                    block_count = floor(20 * i['percent'] / 100)
                    bar = '█' * (block_count if block_count > 0 else 1)
                    content += f'{i["name"]}: ' + \
                                (' ' * (20 - len(i['name']))) + bar + \
                                '░' * (20 - len(bar)) + ' ' + \
                                str(timedelta(seconds=floor(i['total_seconds']))) + \
                                f' {i["percent"]}%' + '\n'
                content += '```\n'
            except KeyError:
                content = f'Block {j} is not allowed'
        self.content += content

    def get_content(self):
        return self.content

    def save_changes(self):
        data = Path('repo/README.md').read_text()
        pattern = f"<!--START_SECTION:waka-->[\\s\\S]+<!--END_SECTION:waka-->"
        new_data = re.sub(pattern=pattern,
                          repl=f'<!--START_SECTION:waka-->\n{self.content}\n<!--END_SECTION:waka-->',
                          string=data)
        Path('repo/README.md').write_text(new_data)
