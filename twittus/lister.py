from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
import json

from twittus.base import manager, CRED, CEND, CORA, MAIN_ACTIONS

ACTIONS = ['add', 'list', 'ls', 'n']
cpl = WordCompleter(ACTIONS + ['quit', 'help'])
history = FileHistory('/tmp/hist.dat')
TWITT = ['twitt', ]


class Lister:
    def __init__(self, api):
        self.api = api
        self.gen = tweets(api)

    def run(self):
        pr = None
        while pr not in MAIN_ACTIONS:
            pr = prompt('twitt-ls>', completer=cpl, history=history,
                        key_bindings_registry=manager.registry).strip()
            if pr == 'n':
                try:
                    txt = next(self.gen)
                    print('{}{}{}'.format(CRED, txt.text, CEND))
                except StopIteration:
                    print('END')
                    pr = '.. cd'
        return pr


def tweets(api):
    for tweet in api.home_timeline():
        yield tweet
