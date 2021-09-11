import pygame as pg
from pygame import mixer
import random as rn
import time as t

#Initialize the pygame
pg.init()

#Create a Screen of Resolution
screen=pg.display.set_mode((800,600))

# Background
background = pg.image.load("space.png")

#Title and Icon
pg.display.set_caption("Space Clash")
icon=pg.image.load("UFO.png")
pg.display.set_icon(icon)

class Player:
    def __init__(self):
        self.Img=pg.image.load('ship.png')
        self.X = 370
        self.Y = 480
        self.X_change=0
        self.Y_change=0

    def Mark(self):  #Marking Player 
        screen.blit(self.Img,(self.X,self.Y))

    def Move(self): #Moving Player
        self.X+=self.X_change
        self.Y+=self.Y_change
        if self.X>736:
            self.X=736
        if self.X<0:
            self.X=0
        if self.Y>536:
            self.Y=536
        if self.Y<0:
            self.Y=0
    def Reset(self):
        self.X = 370
        self.Y = 480
        self.X_change=0
        self.Y_change=0

    def Velocity_Reset(self,x=0,y=0):
        self.X_change=x
        self.Y_change=y

class Enemy:
    def __init__(self,x,y):
        self.X=x
        self.Y=y
        self.Img=pg.image.load('enemy.png')
        self.X_change=0.3
        self.Y_change=40
        
    def Mark(self):  #Marking Enemy
        screen.blit(self.Img,(self.X,self.Y))

    def Move(self):  #Moving Enemy
        if self.X <= 0:
            self.X_change=0.3
            self.Y+=self.Y_change
        if self.X >= 736:
            self.X_change=-0.3
            self.Y+=self.Y_change
        if (self.X>800 or self.Y>600) or (self.X<-20 or self.Y<-20) :  
            self.X,self.Y=200,200
        self.X+=self.X_change

    def Reset(self):
        self.X = rn.randint(0,800)
        self.Y = rn.randint(50,200)

    def Velocity_Reset(self,x=0,y=0):
        self.X_change=x
        self.Y_change=y

class Bullet:
    def __init__(self):
        self.Img=pg.image.load('bullet.png')
        self.X = -30  #initially Bullet is at outer space
        self.Y = -30  #initially Bullet is at outer space
        self.Y_change=0
        self.State="ready"
        self.Sound=mixer.Sound('shoot.wav')

    def Mark(self):
        screen.blit(self.Img,(self.X+24.5,self.Y))  #Bullet from the spaceship

    def Move(self):  #Moving Bullet
        if self.Y<-30:
            self.State="ready"
            self.X=-30
            self.Y=-30
        if self.State=="fired":
            self.Y-=self.Y_change

    def Reset(self):
        self.Y=-30
        self.Y_change=0
        self.State="ready"

    def Velocity_Reset(self,x=0,y=0):
        self.X_change=x
        self.Y_change=y

    def Effect(self):
        self.Sound.play()

    def Release(self,p):
        if self.State=="ready":
            self.X,self.Y=p.X,p.Y
            self.Mark()
            self.Y_change=0.7
            self.State="fired"
            self.Effect()

class Utils:
    def __init__(self):
        #Collide
        self.isCollide=False
        self.Collide_Type=""
        self.Collide_Pt=0.0
        self.Explode_Sound=mixer.Sound('explosion.wav')
        #Burst Anime
        self.BurstX=30
        self.BurstY=30
        self.BurstImg=pg.image.load('burst hollow.png')
        self.Bullet_Enemy_Collide=0
        self.Player_Enemy_Collide=0
        #Others
        self.Score_Value=0
        self.font=pg.font.Font('freesansbold.ttf',22)
        self.Game_Over_font=pg.font.Font('freesansbold.ttf',60)
        self.pause=False
        Bursted=["burst\\burst1.png","burst\\burst2.png","burst\\burst3.png","burst\\burst4.png","burst\\burst5.png","burst\\burst6.png","burst\\burst7.png","burst\\burst8.png","burst\\burst9.png","burst\\burst10.png","burst\\burst11.png"]
        

    def Burst_Anime(self):
        screen.blit(self.BurstImg,(self.BurstX,self.BurstY))  #Marking Burst Area
        self.Explode_Sound.play()                             #Explosion Sound Effects
        
    def Show_Score(self,x=10,y=10): #Marking Score
        Score=self.font.render("Score : "+str(self.Score_Value),True,(255,255,255))
        screen.blit(Score,(x,y))
        
    def Game_Over(self,x=250,y=250,Msg="Game Over"):
        Over=self.Game_Over_font.render(str(Msg),True,(255,255,255))
        screen.blit(Over,(x,y))
        
    def Collision_Handle(self,p,a,b):
        #Collision Theory  @! Distance between two points
        #Setting Collision is False in Initial
        self.isCollide=False
        #
        self.Bullet_Enemy_Collide = ( (a.X-b.X)**2 + (a.Y-b.Y)**2 )**0.5
        self.Player_Enemy_Collide = ( (a.X-p.X)**2 + (a.Y-p.Y)**2 )**0.5

        if self.Bullet_Enemy_Collide<27:
            self.Collide_Type,self.isCollide,self.Collide_Pt="Enemy_Bullet",True,self.Bullet_Enemy_Collide

        if self.Player_Enemy_Collide<45:
            self.Collide_Type,self.isCollide,self.Collide_Pt="Enemy_Player",True,self.Player_Enemy_Collide

        if self.isCollide:    
            if self.Collide_Type=="Enemy_Bullet":              #burst Anime
                self.BurstX=a.X+self.Collide_Pt
                self.BurstY=a.Y+self.Collide_Pt
                self.Score_Value+=1
                self.Burst_Anime()
                b.Reset()
                a.Reset()
            if self.Collide_Type=="Enemy_Player":
                self.Explode_Sound.play()
                mixer.music.pause()
                self.Game_Over()
                self.Game_Over(275,350,"Score : "+str(self.Score_Value))
                pg.display.update()              # Updating Coordinates
                t.sleep(5)
                pg.quit()
            

    

#Sounds
mixer.music.load('bg_music.mp3')   #BG Music
mixer.music.play(-1)               #BG Music Playing Infinity

#Objects
no_of_Enemy=6
Enemies=[]
for i in range(no_of_Enemy):
    Enemies.append(Enemy( rn.randint(20,736),rn.randint(50,200) ))  #6 Enemy
Player1=Player()                                                    #Player
Bullet1=Bullet()                                                    #Bullet
Util=Utils()                                                        #Other Funcs

    

#Main Algo (infinite Loop)
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT :
            pg.quit()
            break
        if event.type == pg.KEYDOWN: #Detect Key Press
            if event.key == pg.K_p:      #pause Logic
                Util.pause = not Util.pause
            if event.key == pg.K_LEFT and (not Util.pause): #Detect KEY Left
                Player1.X_change-=0.7
            if event.key == pg.K_RIGHT and (not Util.pause): #Detect KEY Right
                Player1.X_change+=0.7
            if event.key == pg.K_UP and (not Util.pause): #Detect KEY Up
                Player1.Y_change-=0.5
            if event.key == pg.K_DOWN and (not Util.pause): #Detect KEY Down
                Player1.Y_change+=0.5
            if event.key == pg.K_SPACE and (not Util.pause): #Detect KEY Down
                Bullet1.Release(Player1)
        if event.type == pg.KEYUP:  #Detect KEY Release
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN:
                Player1.Velocity_Reset()

    if Util.pause:
        continue
    
    Player1.Move() #Player Recordinate Algo
    Bullet1.Move() #Bullet Recordinate Algo
    Player1.Mark()  #Showing Player with boundary
    Bullet1.Mark()  #Showing Bullet with Auto-Dejection(out of space)
    for i in Enemies:
        i.Move()
        i.Mark()     #Showing Enemy with boundary
        Util.Collision_Handle(Player1,i,Bullet1)  #Collision Detect(#Distance between two points)
                
    Util.Show_Score()  #Display Scores
    
    pg.display.update()              # Updating Coordinates
