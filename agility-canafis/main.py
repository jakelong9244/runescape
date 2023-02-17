from functions import *
from constants import START,ROOF,MARK
import time as t
import pyautogui
import playsound as ps
import os

hasFallen = False
hasMark = False
roofFound = True
redRoofFound = True
delay = 0

t.sleep(1)

while hasFallen is False:
    for x in range(8):
        delay = randomTiming()
        
        if x == 0:
                clickImage(START)

        else:
            hasMark = clickMark (MARK)

            if hasMark is False:
                roofFound = clickImage(ROOF[x])

                if roofFound is False:
                    if x > 4:
                        continue
                    redRoofFound = clickImage(ROOF[x+7])

                    if redRoofFound is False:
                        hasFallen = True
                        break

            else:
                hasFallen = True
                break

            
            


        t.sleep(delay)

ps.playsound(r"alert-sound.mp3")