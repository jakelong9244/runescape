from functions import *
import time

time.sleep(1)
x = False
counter = 1

while x is False:
    if counter >= 26:
        counter = 0
        print("yogabagaba")
        restock()
    
    counter += findAlcSpell()
    x = stop()

    

