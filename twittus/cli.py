from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from twittus.base import manager, CRED, CEND, CORA, MAIN_ACTIONS

ACTIONS = ['add', 'list', 'ls']
cpl = WordCompleter(ACTIONS + ['quit', 'help'])
history = FileHistory('/tmp/hist.dat')
TWITT = ['twitt', ]


class InitAction:
    def __init__(self, api):
        self.api = api

    def run(self):
        pr = None
        while pr not in MAIN_ACTIONS:
            pr = prompt('twitt>', completer=cpl, history=history,
                        key_bindings_registry=manager.registry)
            pr = pr.strip()
            if pr not in ACTIONS + ['quit']:
                print('{}Options are: {}'.format(CRED, CEND))
            elif(pr == 'add'):
                add = AddAction(self.api)
                pr = add.run()
            elif(pr == 'list'):
                print('List tweets')
            elif(pr == 'ls'):
                print('{}{}{}'.format(CORA, ACTIONS, CEND))


class AddAction:
    def __init__(self, api):
        self.api = api

    def run(self):
        pr = None
        cpl = WordCompleter(ACTIONS + ['quit', 'help'] + TWITT)
        while pr not in MAIN_ACTIONS:
            pr = prompt('twitt:add>', completer=cpl, history=history,
                        key_bindings_registry=manager.registry)
            pr = pr.strip()
            if pr == 'ls':
                print('{}{}{}'.format(CORA, TWITT, CEND))
            if pr.startswith('twitt '):
                commands = pr.split(' ')
                twitt = ' '.join(commands[1:])
                print('Twiiting:', twitt)
                self.api.update_status(status=twitt)
