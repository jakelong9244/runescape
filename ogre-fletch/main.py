from functions import *
import pyautogui as auto
import time as t

stop = False
world = 0
verify = 0

t.sleep(1)
while stop is False:
    if auto.position() == (2579,1439) or world == 53:
        stop = True
        break
    
    clickUg()
    if checkStock() is False:
        world += 1
        if checkWorld(world) is True:
            world += 1
        changeWorld(world)
    else:
        verify = getLogs()
        if verify is not None:
            fletch()