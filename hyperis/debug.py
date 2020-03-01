from termcolor import cprint

def log(msg):
  cprint(f'[DEBUG] {msg}', attrs=['dark'])
