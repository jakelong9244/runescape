import pyautogui as auto
import time as t
import random as r

def findAlcSpell():
    if auto.locateOnScreen(image=r"C:\Users\Jacob\Documents\Python Projects\Runescape\high-alc\high-alc.png",confidence=0.5,region=(2000,1000,560,440)) is not None:
        x,y = auto.locateCenterOnScreen(image=r"C:\Users\Jacob\Documents\Python Projects\Runescape\high-alc\high-alc.png",confidence=0.5,region=(2000,1000,560,440))
        auto.moveTo(x,y,duration=0.1)
        auto.click(clicks=2,interval=0.1)
        t.sleep(randomTiming(200)+1.5)
        return 1
    else:
        t.sleep(randomTiming(100))
        return 0

def stop():
    x,y = auto.position()
    if x == 2559 or y == 1439:
        print("stopped")
        return True
    else:
        return False

def restock():
    auto.moveTo(x=1087,y=734,duration=randomTiming(50))
    auto.click(button="right")
    t.sleep(randomTiming(100)+0.5)
    auto.click(x=1090,y=775,duration=(randomTiming(50)+0.2))

    t.sleep(randomTiming(100)+1)

    auto.moveTo(x=847,y=340,duration=(randomTiming(50)))
    auto.click(button="right")
    t.sleep(randomTiming(50)+0.5)
    auto.click(x=800,y=451,duration=(randomTiming(50)+0.2))

    t.sleep(randomTiming(200))

def randomTiming(x):
    return r.randrange(1,x) * 0.01