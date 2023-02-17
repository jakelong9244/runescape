import pyautogui as auto
import random as r
import time as t

def clickUg():
    if auto.locateOnScreen(image=r"uglug.png",confidence=0.6) is not None:
        x,y = auto.locateCenterOnScreen(image=r"uglug.png",confidence=0.6)

        auto.moveTo(x,y+20,duration=randomTiming(0.1,0.2))
        auto.click(button="right")

        auto.moveTo(x,y+65,duration=randomTiming(0.2,0.4))
        auto.click()
        t.sleep(randomTiming(4,5))


def getLogs():
    if auto.locateOnScreen(image=r"log.png",confidence=0.6) is not None:
        x,y = auto.locateCenterOnScreen(image=r"log.png",confidence=0.6)
        auto.moveTo(x,y,duration=randomTiming(0.1,0.2))
        auto.click(button="right")

        auto.moveTo(x,y+80,duration=randomTiming(0.2,0.4))
        auto.click()

        auto.press("esc")
        return 1
    else:
        return None

def checkStock():
    if auto.locateOnScreen(image=r"out.png",confidence=0.9) is None:
        return True
    else:
        return False

def fletch():
    auto.moveTo(x=2160,y=1120,duration=randomTiming(0.1,0.3))
    auto.click()
    
    auto.moveTo(x=2095,y=1165,duration=randomTiming(0.1,0.3))
    auto.click()
    t.sleep(randomTiming(0.01,0.05))

    auto.moveTo(x=2140,y=1165,duration=randomTiming(0.1,0.15))
    auto.click()

    t.sleep(randomTiming(0.75,1.5))
    auto.press("space")

    t.sleep(randomTiming(46,49))

def changeWorld(x):
    world = 80 + (x*25)
    auto.moveTo(x=2320,y=world,duration=randomTiming(0.3,0.5))
    auto.click(clicks=2,interval=randomTiming(0.1,0.3))
    t.sleep(randomTiming(8,10))

def randomTiming(x,y):
    return r.uniform(x,y)