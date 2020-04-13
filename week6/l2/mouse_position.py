'''
from Xlib import display


def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]


if __name__ == "__main__":
    print("The mouse position on the screen is {0}".format(mousepos()))
'''

import pyautogui, sys, os

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if x < 683 and y < 384:
            duration = 1  # seconds
            freq = 440  # Hz
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
except KeyboardInterrupt:
    print('\n')

#683 384