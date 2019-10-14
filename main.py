import click
import curses
import termcolor
import pyfiglet
import keys
from player import *
from config import window_size

curses.initscr()
win = curses.newwin(*window_size)
curses.noecho()
curses.cbreak()
win.keypad(1)
curses.curs_set(0)

win.clear()
win.border()
win.nodelay(1)

p = Player(win, 'Cléa', atk=80, hp=100)

while True:
    key = win.getch()
    if key in keys.pause:
        #TODO: pause menu
        break
    elif key in keys.down:
        p.move(DOWN)
    elif key in keys.up:
        p.move(UP)
    elif key in keys.right:
        p.move(RIGHT)
    elif key in keys.left:
        p.move(LEFT)
    elif key in keys.interact:
        p.interact()
        
    # p.debug()
    p.render()
    
    