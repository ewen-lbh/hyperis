import click
import curses
import termcolor
import pyfiglet
import keys
from player import Player
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
        p.move('down')
    elif key in keys.up:
        p.move('up')
    elif key in keys.right:
        p.move('right')
    elif key in keys.left:
        p.move('left')
    elif key in keys.interact:
        p.interact()
        
    p.debug()
    
    