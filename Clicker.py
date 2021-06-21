from keyboard import *
from time import sleep
import mouse



run=True
def stop():
    global run
    run=False
    
def clicking():
    while run:
        if mouse.is_pressed(button="right"):
            while True:
                sleep(0.01)
                mouse.double_click(button="right")

add_hotkey('[',clicking)
wait(']', stop)