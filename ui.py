import click
import termcolor
import pyfiglet

def title(style="default"):
    with open('main-title-{}.txt'.format(style), 'r', encoding='utf8') as file:
        return file.read()

from time import sleep
import sys

def typewriter(string, speed=40, method="char"):
    if method == "char":
        delay_next_char = False
        for character in string:
            sleep(1/speed)
            sys.stdout.write(character)
            sys.stdout.flush()
            if character == '\n':
                sleep(1/speed * 4)
            if character == '.':
                delay_next_char = True
            if character == ' ' and delay_next_char:
                sleep(1/speed * 2)
                delay_next_char = False
    elif method == "line":
        for line in string.split('\n'):
            sleep(1/speed)
            sys.stdout.write(line+'\n')
            sys.stdout.flush()
    return string
