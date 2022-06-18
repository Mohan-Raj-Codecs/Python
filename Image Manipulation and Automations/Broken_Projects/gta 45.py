import cv2 as c
import numpy as np
from time import *
from PIL import ImageGrab
from directkeys import PressKey,W,A,S,D,ReleaseKey
import pyautogui

#sleep(3)
#PressKey(W)
#sleep(3)
#ReleaseKey(W)

def roi(img,vertices):
    mask=np.zeros_like(img)
    c.fillPoly(mask,vertices,255)
    masked=c.bitwise_and(img,mask)
    return(masked)

def Graye(x):
    y=c.cvtColor(x,c.COLOR_BGR2GRAY)
    y=c.Canny(y,threshold1=30,threshold2=60)
    return y

def main():
    while True:
        img=np.array(ImageGrab.grab(bbox=(0,40,785,590)))
        im=Graye(img)
        #c.imshow('copy',c.cvtColor(img,c.COLOR_BGR2RGB))
        #c.imshow('copy',im)
        verti=np.array([[0,590],[0,390],[197,250],[589,250],[785,390],[785,590]])
        musk=roi(im,[verti])
        c.imshow('mask',musk)
        k=c.waitKey(1)
        if k==ord('q'):
            break

main()
c.destroyAllWindows()
