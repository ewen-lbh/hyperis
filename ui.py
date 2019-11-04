import click
import termcolor
import pyfiglet

def title(style="default"):
    with open('main-title-{}.txt'.format(style), 'r', encoding='utf8') as file:
        print(file.read())

from time import sleep
import sys

def typewriter(string, speed=30):
    delay_next_char = False
    for character in string:
        sleep(1/speed)
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == '\n':
            sleep(1)
        if character == '.':
            delay_next_char = True
        if character == ' ' and delay_next_char:
            sleep(0.5)
            delay_next_char = False
    return string
