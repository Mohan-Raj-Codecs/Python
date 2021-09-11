import pyautogui as p
from time import *
sleep(4)
def st():
    p.hotkey('space')
    print('Started Game!!')
def re():
    sop=p.locateCenterOnScreen('my.png')
    if sop is None :
        print('Game ended')
    else :
        pass

'''def sec():
    tomes=list(asctime())
    se_=str(tomes[17:19])
    s=se_[2]
    s+=se_[7]
    se=int(s)  #here is seconds extract se
    mi_=str(tomes[14:16])
    m=mi_[2]
    m+=mi_[7]
    mi=int(m)  #here is minutes extract  mi
'''

#alertdino=[738,324]
#coluurs  ngrey=[172,172,172],grey=[83,83,83],white=[255,255,255],black=[0,0,0]
def bot():
    while True :
        no_obj=[255,255,255]
        a_obj=[83,83,83]
        tome=int(perf_counter())
        cactus=list(p.pixel(722,330))
        crow=list(p.pixel(727,280))
        #if tome>56.5 :
           # no_obj=[0,0,0]
            #a_obj=[172,172,172]
        if cactus==a_obj :
            p.press('space')
            sleep(0.13)
            p.press('down')
        if crow==a_obj :
            p.press('space')
            p.press('space') # Wondering Why Pressing Two Space ,
            sleep(0.2)       # Just To Make Double Ensure That Dino Jumps 
            p.press('down')
bot()
#perf_counter()
