#!/bin/env python2
from pykeyboard import PyKeyboard
from time import sleep
from random import choice
import sys
if len(sys.argv) < 2:
    print 'Usage: "./auto2048.py <strategy> [delay in seconds]"\n'\
            'Then focus on the browser window in which you are playing 2048.\n'\
            'Strategies include:\n'\
            ' - cycle:      cycles up, down, left, right\n'\
            ' - upcyc:      cycle left, up, right, up\n'\
            ' - corners:    cycle through corners\n'\
            ' - random:     press keys at random\n'\
            ' - upright:    goes up and to the right, presses left key once\n'\
            '               every 20 moves, may get stuck and need down key pressed\n'\
            '               manually. Probably the best strategy.\n'\
            'To quit, select this window and press Ctrl+C'
    exit()
strat = sys.argv[1]
k = PyKeyboard()
if len(sys.argv) < 3:
    delay = 0.1
else:
    delay = float(sys.argv[2])
keys = [k.up_key, k.down_key, k.right_key, k.left_key]
def cycle():
    k.tap_key(k.left_key)
    sleep(delay)
    k.tap_key(k.down_key)
    sleep(delay)
    k.tap_key(k.right_key)
    sleep(delay)
    k.tap_key(k.up_key)
    sleep(delay)
x = 15
def upcyc():
    k.tap_key(k.left_key)
    sleep(delay)
    k.tap_key(k.up_key)
    sleep(delay)
    k.tap_key(k.right_key)
    sleep(delay)
    k.tap_key(k.up_key)
    sleep(delay)
def corners():
    c = 0
    while c < x:
        k.tap_key(k.left_key)
        sleep(delay)
        k.tap_key(k.up_key)
        sleep(delay)
        c+=1
    c = 0
    while c < x:
        k.tap_key(k.up_key)
        sleep(delay)
        k.tap_key(k.right_key)
        sleep(delay)
        c+=1
    c = 0
    while c < x:
        k.tap_key(k.right_key)
        sleep(delay)
        k.tap_key(k.down_key)
        sleep(delay)
        c+=1
    c = 0
    while c < x:
        k.tap_key(k.down_key)
        sleep(delay)
        k.tap_key(k.left_key)
        sleep(delay)
        c+=1
def randupleft():
    v = 0
    while v < 20:
        k.tap_key(k.up_key)
        sleep(delay)
        k.tap_key(k.right_key)
        sleep(delay)
        v+=1
    k.tap_key(choice([k.up_key, k.left_key, k.right_key]))
    sleep(delay)
def random():
    k.tap_key(choice(keys))
    sleep(delay)
if __name__ == "__main__": 
    while True:
        getattr(sys.modules[__name__], strat)()
