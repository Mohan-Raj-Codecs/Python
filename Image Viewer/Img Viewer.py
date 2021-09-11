import os
from tkinter import *
from PIL import ImageTk, Image

class ImgDetect:
    def __init__(self):
        self.Files=[]
        self.Photo_Files=[]
        self.Photo_Objects=[]
        self.Photo_Extensions=['jfif','bmp','dib','eps','gif','icns','ico','im','jpeg','jpg','msp','pcx','png','xpm','wmf','gbr','wal','psd','pixar','pcd','mpo','mic','mcidas','naa','iptc','imt','gd','gbr','ftex','fpx','flc','fli','dds','dcx','cur','blp','xbm','webp','tiff','tga','spider','sgi','ppm']
        self.Current_File=''
        self.Filename=''
        self.Current_Pos=0
        self.Res='700x700'
        self.button_forward=0
        self.button_back=0
        self.button_reset=0
        self.button_exit=0
        self.label=0
        self.root=0                  #Initializing Window
        
    def direc(self,path=''):
        if path=='':                            #If Path Not Listed
            self.Files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for File in self.Files:
                extension = File[File.rfind('.')+1:]  #Skipping (.) from extension
                for i in self.Photo_Extensions:                       #Iterating Photo Extension Possibilities
                    if (i==extension) and not(File=='cant.png') :              #Photo Extension = My Extension
                        self.Photo_Files.append(File)           #Then Add it to Photo Files for Projecting it
        else:                                       #### If Path is Entered By User add it to log and Start searching with that #####!! Handle Here !!####
            pass                                    #### and Too Change the Directory to That Path  and also list the old directory Files ###!!!!

        if len(self.Photo_Files)==0:
            self.Photo_Files=['cant.png']                                  #If No Photo Files Found
            
        self.Current_File=self.Photo_Files[0]   #Setting Initial Setting
        self.Current_Pos=0                      #Setting Initial Setting

    def back(self):
        self.Current_Pos-=1
        self.update()
            
    def forward(self):
        self.Current_Pos+=1
        self.update()
            
    def resizer(self,Res='700x700'):
        self.Res=Res
        self.root.geometry(self.Res)
        
    def display(self):
        self.root=Tk()   #Initializing Tkinter
        self.root.configure(bg='white')
        
        for i in self.Photo_Files:                                  #Creating Photo Objects
            self.Photo_Objects.append(ImageTk.PhotoImage(Image.open(i)))     
            
        self.root.title("Image Viewer")
        self.resizer()

        #DISPLAY VALUES
        self.button_back = Button(self.root, text="Back", command=self.back ,state=DISABLED)
        self.button_forward = Button(self.root, text="Forward", command=self.forward ,state=NORMAL)
        self.button_exit = Button(self.root, text="Exit", command=self.root.destroy)
        self.button_reset = Button(self.root, text="Refresh List", command=self.reset)
        self.label = Label(image=self.Photo_Objects[self.Current_Pos])
        self.Filename = Label(self.root, text=self.Current_File , font='Arial 10')

        #GRIDING VALUES
        self.Filename.grid(row=1,column=0,columnspan=4)
        self.label.grid(row=2, column=0, columnspan=4)
        self.button_back.grid(row=5, column=0)
        self.button_exit.grid(row=5, column=1)
        self.button_reset.grid(row=5, column=2)
        self.button_forward.grid(row=5, column=3)

        self.update()

        self.root.mainloop()

    def update(self):
        #FLUSHING VALUES
        self.label.config(image='')  #Flushing Label to Display None :)
        self.Filename.config(text='')

        #UPDATING
        self.Current_File=self.Photo_Files[self.Current_Pos]

        if self.Current_Pos<=0:          #back
            self.button_back.config(state = DISABLED)
        else:
            self.button_back.config(state = NORMAL)
            
        if self.Current_Pos >=  len(self.Photo_Objects)-1:   #forward
            self.button_forward.config(state = DISABLED)
        else:
            self.button_forward.config(state = NORMAL)

        ##WINDOWS Height and Width Logic
        width,height = Image.open(self.Photo_Files[self.Current_Pos]).size
        rez=2
        while width>1000 or height>700 :                         #Resizing with Aspect ratio Immunity 
            width,height=round(width//rez),round(height//rez)
            print('yeah Iterating : ',width,'x',height)
            rez-=0.1

        self.Photo_Objects[self.Current_Pos]=ImageTk.PhotoImage( Image.open(self.Current_File).resize( (width,height) ))
        height+=60   #For Options
        self.resizer(str(width)+'x'+str(height)) #Adapt Photo Size to Windows Size

        #REFILLING VALUES
        self.label = Label(image=self.Photo_Objects[self.Current_Pos])
        self.Filename = Label(self.root, text=self.Current_File ,font='Arial 10')

        #GRIDING IN GUI
        self.Filename.grid(row=1,column=0,columnspan=4)
        self.label.grid(row=2, column=0, columnspan=4)
        self.button_back.grid(row=5, column=0)
        self.button_exit.grid(row=5, column=1)
        self.button_reset.grid(row=5, column=2)
        self.button_forward.grid(row=5, column=3)

    def reset(self):
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


