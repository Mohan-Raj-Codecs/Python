import os
from tkinter import *
from PIL import ImageTk, Image
from time import sleep
import subprocess as sp

sp.call("Screenshot.bat",shell=True)
pixel_width,pixel_height=Image.open("screenshot.png").size
MAX_RIGHT,MAX_DOWN,MAX_LEFT,MAX_UP=(0,0,0,0)

def Phone_Info():
    pixel_width,pixel_height=Image.open("screenshot.png").size
    MAX_RIGHT=pixel_width,pixel_height//2
    MAX_DOWN=pixel_width//2,pixel_height
    MAX_LEFT=1,pixel_height//2
    MAX_UP=pixel_width//2,1

class ImgDetect:
    def __init__(self):
        self.Files=[]
        self.Photo_File="screenshot.png"
        self.Photo_Object=None
        self.Photo_Extensions=['jfif','bmp','dib','eps','gif','icns','ico','im','jpeg','jpg','msp','pcx','png','xpm','wmf','gbr','wal','psd','pixar','pcd','mpo','mic','mcidas','naa','iptc','imt','gd','gbr','ftex','fpx','flc','fli','dds','dcx','cur','blp','xbm','webp','tiff','tga','spider','sgi','ppm']
        self.scale_fact=0
        self.click_press_X=0
        self.click_press_Y=0
        #Buttons
        self.button_home=0
        self.button_menu=0
        self.button_back=0
        self.button_reset=0
        self.button_refresh=0
        #Buttons END
        self.label=0
        self.root=0                  #Initializing Window
        self.canvas=0
        
    def direc(self,path=''):
        if path=='':                            #If Path Not Listed
            self.Files = [f for f in os.listdir('.') if os.path.isfile(f)]  
            if (self.Photo_File in  self.Files) and not('cant.png' in self.Files) :              #Photo Extension = My Extension
                self.Photo_File=self.Photo_File
            else:
                self.Photo_File="cant.png"

    def back(self):
        sp.call("adb shell input keyevent KEYCODE_BACK",shell=True)
        self.update()
            
    def home(self):
        sp.call("adb shell input keyevent KEYCODE_HOME",shell=True)
        self.update()

    def menu(self):
        sp.call("adb shell input keyevent KEYCODE_MENU",shell=True)
        self.update()

    def upscale(self,width,height):
        print("Upscaled  : ",width*self.scale_fact,height*self.scale_fact)
        global pixel_width,pixel_height
        if (width*self.scale_fact>pixel_width) or (height*self.scale_fact>pixel_height):
            print("Over")
            return -1,-1
        return width*self.scale_fact,height*self.scale_fact

    def click_press(self,event):
        print("Rooted : ",event.x_root,event.y_root)
        x,y=self.upscale(event.x,event.y)
        self.click_press_X=x
        self.click_press_Y=y

    def click_release(self,event):
        x,y=self.upscale(event.x,event.y)
        cm=""
        if (self.click_press_X<0 and x<0) and (self.click_press_Y<0 and y<0):
            print("OutofBound")
            return #OutBout Click and Drags
        
        elif self.click_press_X==x and self.click_press_Y==y:
            print("Click")
            cm="adb shell input tap "+str(round(x))+" "+str(round(y))

        else:
            print("Swipe")
            cm="adb shell input swipe "+str(round(self.click_press_X))+" "+str(round(self.click_press_Y))+" "+str(round(x))+" "+str(round(y))
        
        print(self.click_press_X,x,self.click_press_Y,y)
        #print(cm)
        #cm="adb shell input tap "+str(round(x))+" "+str(round(y))
        sp.call(cm,shell=True)
        self.update()
        
        
    def resizer(self,width=480,height=800):
        rez=2
        ori_width=width
        while width>1000 or height>700 :                         #Resizing with Aspect ratio Immunity 
            width,height=round(width//rez),round(height//rez)
            print('yeah Iterating : ',width,'x',height)
            rez-=0.1
        print("Upscale Fact  : ",self.scale_fact)
        self.Photo_Object=ImageTk.PhotoImage(Image.open("screenshot.png").resize( (width,height) ))
        self.root.geometry(str(width+100)+'x'+str(height))
        self.scale_fact=ori_width/width
        
    def display(self):
        self.root=Tk()   #Initializing Tkinter
        self.root.bind('<ButtonPress-1>',self.click_press)
        self.root.bind('<ButtonRelease-1>',self.click_release)
        self.root.configure(bg='white')

        self.Photo_Object=ImageTk.PhotoImage(Image.open("screenshot.png"))
            
        self.root.title("Image Viewer")
        width,height = Image.open("screenshot.png").size
        self.resizer(width,height)

        #DISPLAY VALUES
        self.button_back = Button(self.root, text="Back", command=self.back ,state=NORMAL)
        self.button_home = Button(self.root, text="Home", command=self.home ,state=NORMAL)
        self.button_menu = Button(self.root, text="Menu", command=self.menu ,state=NORMAL)
        self.button_refresh = Button(self.root, text="Refresh\nScreen", command=self.update ,state=NORMAL)
        self.button_reset = Button(self.root, text="Screen\nFix", command=self.reset)
        self.label = Label(image=self.Photo_Object)

        #GRIDING VALUES
        self.label.grid(row=0, column=0, columnspan=4,rowspan=5)
        self.button_back.grid(row=0, column=6)
        self.button_home.grid(row=1, column=6)
        self.button_menu.grid(row=2, column=6)
        self.button_refresh.grid(row=3, column=6)
        self.button_reset.grid(row=4, column=6)
        

        self.update()

        self.root.mainloop()

    def update(self):
        Phone_Info() #Outer Func call
        #Updating Screenshot from ADB
        sleep(0.5)
        sp.call("Screenshot.bat",shell=True)
        #FLUSHING VALUES
        self.Photo_Object=ImageTk.PhotoImage(Image.open("screenshot.png"))
            
        self.root.title("Image Viewer")
        width,height = Image.open("screenshot.png").size
        self.resizer(width,height)

        #DISPLAY VALUES
        self.button_back = Button(self.root, text="Back", command=self.back ,state=NORMAL)
        self.button_home = Button(self.root, text="Home", command=self.home ,state=NORMAL)
        self.button_menu = Button(self.root, text="Menu", command=self.menu ,state=NORMAL)
        self.button_refresh = Button(self.root, text="Refresh\nScreen", command=self.update ,state=NORMAL)
        self.button_reset = Button(self.root, text="Screen\nFix", command=self.reset)
        self.label = Label(image=self.Photo_Object)

        #GRIDING VALUES
        self.label.grid(row=0, column=0, columnspan=4,rowspan=5)
        self.button_back.grid(row=0, column=6)
        self.button_home.grid(row=1, column=6)
        self.button_menu.grid(row=2, column=6)
        self.button_refresh.grid(row=3, column=6)
        self.button_reset.grid(row=4, column=6)

    def reset(self):
        Phone_Info()
        self.root.destroy()
        self.__init__()                          # Using Constructor as a Destructor   :)
        self.direc()
        self.display()
        



cu=ImgDetect()
cu.direc()
cu.display()


#c.destroyAllWindows()


#Arrow Controls photo transition
#Build a image amplifier Maintain Aspect Ratio of Picture (Height to mmaintain at 700 px and corresponding width)


