import random
import time
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys


MAIN_ACTIONS = ['cd ..', 'cd', 'quit']
WORDS = ['ls', 'del', 'help'] + MAIN_ACTIONS
CRED = '\033[91m'
CEND = '\033[0m'
CBLUE = '\033[34m'
CGRE = '\033[32m'
CORA = '\033[93m'

random.seed(time.time())
bye_bye = ['Sayonara', 'Auf Wiedersehen', 'Adeus', 'Au revoir', 'Addio']
manager = KeyBindingManager.for_prompt()


@manager.registry.add_binding(Keys.ControlC)
@manager.registry.add_binding(Keys.ControlD)
def _(event):
    print('{}!'.format(random.choice(bye_bye)))
    event.cli.set_return_value('quit')
