from termcolor import cprint
from hyperis import constants

def log(msg):
  if constants.DEBUG_MODE:
    cprint(f'[DEBUG] {msg}', attrs=['dark'])
