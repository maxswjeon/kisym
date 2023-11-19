import curses
import math
import os
import time

import pandas as pd

CURRENT_DIR = "."
FILE_PATH = ""

stdscr = None


def init():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.keypad(True)
    curses.cbreak()


def main():
    stdscr.clear()
    stdscr.addstr(0, 0, "KiCAD Symbol Generator")
    stdscr.refresh()

    available_functions = []

    if FILE_PATH == "":
        pass

    time.sleep(5)


if __name__ == "__main__":
    init()
    main()
    curses.endwin()
