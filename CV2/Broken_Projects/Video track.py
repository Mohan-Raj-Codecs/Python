import cv2 as c
import numpy as np

def nothing(x):
    pass

cap=c.VideoCapture(0)

c.namedWindow('Tracking')
c.createTrackbar('LH','Tracking',0,255,nothing)
c.createTrackbar('LS','Tracking',0,255,nothing)
c.createTrackbar('LV','Tracking',0,255,nothing)
c.createTrackbar('UH','Tracking',255,255,nothing)
c.createTrackbar('US','Tracking',255,255,nothing)
c.createTrackbar('UV','Tracking',255,255,nothing)

while True:
    ret,frame=cap.read()

    hsv = c.cvtColor(frame,c.COLOR_BGR2HSV)

    l_h=c.getTrackbarPos('LH','Tracking')
    l_s=c.getTrackbarPos('LS','Tracking')
    l_v=c.getTrackbarPos('LV','Tracking')
    
    u_h=c.getTrackbarPos('UH','Tracking')
    u_s=c.getTrackbarPos('US','Tracking')
    u_v=c.getTrackbarPos('UV','Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask= c.inRange(hsv,l_b,u_b)

    res=c.bitwise_and(frame,frame,mask=mask)

    c.imshow('frame',frame)
    c.imshow('mask',mask)
    c.imshow('res',res)

    key=c.waitKey(1)
    if key==ord('q'):
        break

cap.release()
c.destroyAllWindows()
