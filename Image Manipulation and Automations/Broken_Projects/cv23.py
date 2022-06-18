import cv2 as c
from time import *
import numpy as np
ca=c.VideoCapture(0)
def camopen():
    while True :
        r,fr=ca.read()
        c.imshow('Came',fr)
        aw=c.waitKey(1)
        if aw==ord('q'):
            break
def click_e(event,x,y,flags,param):
    if event == c.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        c.circle(img,(x,y),3,(0,0,255),-1)
        myco[x,y]=[blue,green,red]
        c.imshow('ours',myco)

img=c.imread('ab.png')
myco=np.zeros((512,512,3),np.uint8)
c.imshow('image',img)
points=[]
c.setMouseCallback('image',click_e)
c.waitKey(0)
c.destroyAllWindows()




                           #cv2.imread()

#var=cv2.imread() This function reads the image specified in it
#var=cv2.imread('x',y) #x='image name jpg or png',y= 1 or 0 or -1
#y indicates how to read the image
#if y=1 then it reads the image with colors
#if y=0 then it reads the image with grayscale
#if y=-1 then it reads the image as it has with alpha chanel and colors
#if x= 'wrong path ' then it returns None

                            #cv2.imshow()
#It Display the image which is read already
#cv2.imshow('x',y)# x='name of window' can be any nickname, y=readed image variable
#it will show image in milli second and fades
#so we have #cv2.waitKey(x)#x=milliseconds #1 second=1000
#if x=0 then it waits for the infinity time
#This function will allow to wait the windows before fades to specified seconds
#Another function is there to destroy the window
#You should not use this function if u are not using the waitkey() function
#cv2.destroyAllWindows() #This will destroy the windows which image is shown

                             #cv2.imwrite()

#cv2.imwrite('x',y)#x='nick name of image tobe saved',y = image variable stored
#This functions allow u to save the image u want

                             #cv2.VideoCapture()

#var=cv2.VideoCapture('x') #x= 'videofilepath.mp4' or 0 or -1
#we can define the function to play already captured file and
#we can tell it to stream live from camera by setting it 0 or -1
#0 is Default
#This Command will play or live stream the file specified

  #r,frame=var.read()

#the video is recorded by frame variable declared
#r will save the progress True or False isit recording
#This Method is used to the var which is recordingthe video by camera
#and we have option for it to read the files in it to video
#r,frame=var.read() reads the file and sends it to the frame variable

#############################################################################
#                   THIS IS OPTIONAL IF U WANT MORE COLOR
            
   #If u want to convert the images to BGR to grayscale or grayscale to BGR
  #There is function to that to convert #abbreviation = #cvt=convert
   #Example : #The default is BGR Format
 #         frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY
#          cv2.imshow('x',frame2)

#############################################################################


  #cv2.imshow('x',frame or frame2 ) refer before
#this is declared to project the processed files

  #aaw=cv2.waitKey(1) refer before in cv2.imread() section
#this will wait for the window to close after 1 milli but it ope on next iteration
#we want to declare what key press to exit otherwise it will infinite and error
#we can get the waitkeys key will variable declared to it
#so here it aaw  see the example to stop this
#  ''' LOOP :
#          aaw=c.waitKey(1)
#          if aaw==ord('q') :
 #             break'''

   #var.release()
#It will release the file tied this is compulsory

   #cv2.destroyAllWindows()
#it will closeall the windows containing image

#HERE IS EXAMPLE TO USE THE VIDEOCAPTURE()
#  '''
  #    ca=c.VideoCapture(0)
 #     while True :
   #       r,fr=ca.read()
      #    c.imshow('Came',fr)
     #     aw=c.waitKey(1)
    #      if aw==ord('q'):
   #               break
  #  
 #     ca.release()
#      c.destroyAllWindows()
#'''

##############################################################################
#     SHAPES TO DRAW ON IMAGE

#Let us captured img read matrix be ra
#Then,overwritting the image to,
# ra=cv2.line(ra,start,end,color(BGR),thick)
#ra=imageread,start = starting axis,end=ending axis,color=(255,0,0),thick=1 or any int
#
#EXAMPLE to draw line :
#         ra=cv2.line(ra,(0,0),(255,255),(255,0,0),4)
#         cv2.imshow('image',ra)
#
#ra=cv2.line(ra,start,end,color(BGR),thick) #Line
#ra=cv2.arrowedLine(ra,start,end,color(BGR),thick) #ARROWED LINE
#ra=cv2.rectangle((ra,start,end,color(BGR),thick)) #Rectangle
#               start--------
#               |            |
#               |            |    #rectangle
#               |            |
#               -----------end
#
#if thickness u give -1  ie.(thickness=-1) then the shape u defined is filled with color  
#
#
#
#ra=cv2.circle((ra,center,radius,color(BGR),thick)) #CIRCLE
#      other arguments are two elements in tuple but radius should be int     
#
#
#font=cv2.FONT_HERSHEY_SIMPLEX#FONT FOR  TEXT
#line=cv2.LINE_AA
#ra=cv2.putText(ra,'text any',start(1,2),font,fontsize,color(BGR),thickness,line) #TEXT
#
#
##########################SEE VIDEO TO UNDERSTAND MOUSE CLICK EVENTS HERE HINTS########
#
#we have to declare a function with parameters(event,x,y,flags,param)
#Then write our code 
#
#outside def we have to declare the img to open and we should call a func() to
#get arguments to our function
#cv2.setMouseCallback('window name',func() name)
#This function will give essential arguments to our func()
#Then we have to declare waitkey and destroy windows
###################################################################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#






























