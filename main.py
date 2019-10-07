import click
import curses
import termcolor
import pyfiglet
from keys import *


window_size = (80, 80)  # (cols, rows)

win = curses.newwin(*window_size)
curses.noecho()
curses.cbreak()
win.keypad(1)
curses.curs_set(0)

win.clear()
win.border()
win.nodelay(1)

while True:
    key = win.getch()
    if key in keys.pause:
        #TODO: pause menu
        break
    elif key in keys.down:
        player.move('down')
    elif key == curses.KEY_UP