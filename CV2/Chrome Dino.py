import pyautogui as p
from time import *
sleep(4)

#alertdino=[738,324]
#coluurs  ngrey=[172,172,172],grey=[83,83,83],white=[255,255,255],black=[0,0,0]
def bot():
    while True :
        no_obj=[255,255,255]
        a_obj=[83,83,83]
        tome=int(perf_counter())
        cactus=list(p.pixel(722,330))
        crow=list(p.pixel(727,280))
        if cactus==a_obj :
            p.press('space') 
            sleep(0.15)
            p.press('down') # This Will Bring Dino Down From Instant Air Time
        if crow==a_obj :
            p.press('space') # Wondering Why Pressing Two Space ,
            p.press('space') # This is Just a Trick to Increase Dino Air Time 
            sleep(0.2)
            p.press('down')  # This Will Bring Dino Down From Air Time 
            
bot()
