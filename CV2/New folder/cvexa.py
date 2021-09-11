import cv2 as c
from time import *
import numpy as np

def cam():
    ca=c.VideoCapture(0)
    mo=c.imread('mo.png',-1)
    while True :
        r,fr=ca.read()
        if mo in fr :
            print('Found Mohan')
            ca.release()
            c.destroyAllWindows()
        c.imshow('Came',fr)
        aw=c.waitKey(1)
        if aw==ord('q'):
            break
    ca.release()
    c.destroyAllWindows()


moh=c.imread('mo.png',-1)
c.imshow('moh',moh)
c.waitKey(0)
c.destroyAllWindows()
