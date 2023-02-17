import pyautogui as auto
import random as rdm
from constants import AREA

def findImage(image):
    if auto.locateOnScreen(image,confidence=0.75) is None:
        return None, None
    else:
        return auto.locateCenterOnScreen(image,confidence=0.75)

def clickCoord(x,y):
    auto.moveTo(x,y,duration=0.2)
    auto.click()

def clickImage(image):
    x,y = findImage(image)
    if x is None and y is None:
        return False
    else:
        clickCoord(x,y)
        return True

def clickMark(image):
    if auto.locateOnScreen(image,confidence=0.20,region=AREA) is None:
        return False
    else:
        x,y = auto.locateCenterOnScreen(image,confidence=0.20,region=AREA)
        auto.moveTo(x,y,duration=0.2)
        auto.click()

def checkFall(var):
    if var is True:
        return False
    else:
        return True

def randomTiming():
    x = rdm.randrange(1,200)
    return (7+x*0.01)
