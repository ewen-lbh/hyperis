import click
import termcolor
import pyfiglet

def title(style="default"):
    with open('main-title-{}.txt'.format(style), 'r', encoding='utf8') as file:
        print(file.read())

