import re
from datetime import timedelta
from math import floor

from gh import GitHubManager
from pathlib import Path

from waka import Wakatime


class ReadmeEditor:
    manager: GitHubManager
    wakatime: Wakatime

    def __init__(self, manager: GitHubManager, wakatime: Wakatime):
        self.manager = manager
        self.wakatime = wakatime
        self.blocks = Path('repo/waka_blocks.txt').read_text().split('\n')
        self.content = ''

    def asd(self):
        return self.blocks

    def generate_data(self):
        content = ''
        blocks = ['editors', 'languages']

        for j in blocks:
            content += f'## {" ".join(j.split("_")).capitalize()} used in the last week\n'
            content += '``` text\n'
            os = self.wakatime.user_stats()['data'][j]
            for i in os:
                block_count = floor(20*i['percent']/100)
                bar = '█' * (block_count if block_count > 0 else 1)
                content += f'{i["name"]}: ' + \
                           (' '*(20-len(i['name']))) + bar + \
                           '░' * (20-len(bar)) + ' ' + \
                           str(timedelta(seconds=floor(i['total_seconds']))) + \
                           f' {i["percent"]}%' + '\n'
            content += '```\n'
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
