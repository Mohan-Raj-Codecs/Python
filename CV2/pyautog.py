"""
Just Pyautogui Tut with Examples
"""
import pyautogui as m
from time import *
sleep(3)

def draw():
    pyautogui.click() 
    di=400
    while di>0 :
        pyautogui.dragRel(di,0,duration=0.2) 
        di-=50
        pyautogui.dragRel(0,di,duration=0.2)
        pyautogui.dragRel(-di,0,duration=0.2)
        di-=50
        pyautogui.dragRel(0,-di,duration=0.2)
def locq():
    sleep(0.1)
    x,y=pyautogui.locateCenterOnScreen('Capture.png')
    pyautogui.dragRel(x,y,duration=0.2)

asa=list(m.locateCenterOnScreen('q.png'))
m.moveTo(asa[0],asa[1],duration=2)

#Mouse :
    #1#pyautogui.click() facilitate a just one click from the mouse online
    #2#pyautogui.click(x,y) facilitates a click from the origin destination to axis mentioned

    #1#pyautogui.dragRel(x,y,duration) #x = x axis,y = y axis,duration = 'in seconds to drag'
    #drags to specified digits from the mouse online
    #2#pyautogui.dragTo(x,y,duration) #x = x axis,y = y axis,duration = 'in seconds to drag'
    #drags to specified digits from the origin to destination mentioned

    #1#pyautogui.moveTo(x,y,duration) #x = x axis,y = y axis,duration = 'in seconds to drag'
    #move to specific digits from origin
    #2#pyautogui.moveRel(x,y,duration) #x = x axis,y = y axis,duration = 'in seconds to drag'
    #move to specific digits from the mouse online

    #pyautogui.position() # provides the position of the mouse

    #pyautogui.scroll(x) #x= how many pixels
    #scrolls upto the given pixels
    #negative sign implies to scroll down and positive to scroll up

#Screen :
    #pg.displayMousePosition() #This will display the real time mouse position with rgb color codes

    # pyautogui.locateCenterOnScreen('x') #x = 'image.png file to find'
    # This will find the center position #()# of the image passed to it
   
    #pg.locateOnScreen('x')#x = 'image.png file to find'
    # This will find the center position #()# of the image passed to it
    #U should declare pg.center(x) #x=pg.locateOnscreen()
    #U should pass the parameter to center as locatescreen because it(center()) only finds
    #what is center point of the founded image

    #x=pg.screenshot() #This will take screenshot and return it to the x variable
    #This should be saved
    #x.save("name.jpg") #This saves the image with name passed to it
    
    #pg.pixel(x,y) #x=x axis,y=y axis
    #Returns the rgb color of the pixel passed
    
    #pg.size() #returns the resolution of screen
    
    

#Keyboard :
    #pyautogui.press(x) facilitate a strike of one key at time
    #x='string'

    #pg.keyDown(x) #x=any hotkeys
    #pg.keyDown will make infinitily key pressed so on
    #pg.keyUp(x) #x=any hotkeys
    #It will release the key pressed in keyDown()

    #pyautogui,typewrite(x,y) #x='string',y = time of each key pressed in seconds
    #facilitate a strike of multiple keys at one by one in milliseconds gap
    #you can use \n to press enter key

    #pg.hotkey(x,y,z,...) #x='ctrl' ,x='a' #Use 'stringed parameters'
    #hotkeys allow to press keys like function ctrl winkey shift capslock tab
    #U can also pass a normal words or strings to it
    #u can declare multiple keys at same time to press it simultaneously
