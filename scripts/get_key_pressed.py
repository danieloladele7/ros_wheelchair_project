#!/usr/bin/python3
import sys

import termios
import tty # teletype writer
    
def getKey(settings):
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def saveTerminalSettings():
    return termios.tcgetattr(sys.stdin)

def restoreTerminalSettings(old_settings):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def executeKey(key):
    print('You pressed {} on the keyboard'.format(key))

def main():
    settings = saveTerminalSettings()
    
    try:
        while True:
            key = getKey(settings)
            # print(type(key))
            if key == "X":
                break
            executeKey(key)
    
    except Exception as e:
        print(e)
    
    finally:
        restoreTerminalSettings(settings)

if __name__ == '__main__':
    main()