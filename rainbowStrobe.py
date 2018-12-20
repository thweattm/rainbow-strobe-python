#!/usr/bin/python3
from blinkt import set_pixel, set_brightness, show, clear, set_all
from time import sleep
from random import randint

clear()
show()
set_brightness(1)
n = 0

while True:
    if (n == 0):
        n = randint(3,10)
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
    else:
        n -= 1
        
    set_all(r,g,b)
    show()
    t = randint(1,15)/100
    sleep(t)
    clear()
    show()
    t = randint(1,15)/100
    sleep(t)
