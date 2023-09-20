"""
A game that calculates the word per minute of the user using time library
Curses library is used to change the color of the text if user type correctly or wrong
Sentences is randomly chosen from a file
The game ends if all characters are typed in correctly
"""
import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()  # clear the window output
    stdscr.addstr("Hello world!")  # (row_index, column_index, output_txt, style)
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()  # wait for user to type any key before exiting the program

# overlay function
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    # get the index(i) and element(char) from current list
    # add the char at the row_index 0 to overlay the printed target text
    for i, char in enumerate(current):
        # check if the current char is similar to target char, if yes display in green if not display in red
        correct_char = target[i]
        color = curses.color_pair(2)
        if char != correct_char:
            color = curses.color_pair(1)

        stdscr.addstr(0, i, char, color)

# get a random sentence from a file
def load_text():
    with open("sentences.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()  # strip will separate the sentences after \n separator

# WPM function
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    # this will ensure the elapsed time is continuously calculated
    stdscr.nodelay(True)
    # add keys pressed by user into current_text
    while True:
        # we get the max value to avoid having a 0 div error at the start
        elapsed_time = max(time.time() - start_time, 1)
        """ len(current_text) / (elapsed_time / 60) get us the character per minute
        assuming the average word has 5 character to get the word per minute"""
        wpm = round((len(current_text) / (elapsed_time / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        """ Since getkey() will require an input and stdscr.nodelay(True) will continue the program it will cause input
        error, so we need to pass in the error by implementing the try, except function """
        try:
            key = stdscr.getkey()
        except:
            continue

        # check if user press 'esc' to exit the loop
        if ord(key) == 27:  # ordinal value of 'esc' in  ASCII is 27
            break
        """ Since curses library has a special case where it does not overwrite a letter if you pressed back space we 
        need to do it manually """
        # check if user pressed backspace
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            # remove the last element in the current_text list
            if len(current_text) > 0:
                current_text.pop()
        # check if we reached the end of the word to be typed
        elif len(current_text) < len(target_text):
            current_text.append(key)

    
# main function
def main(stdscr):  # stdscr = standard screen
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # red text in white bg with index 1
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # second pair of output color
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # second pair of output color

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the test! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break


wrapper(main)
