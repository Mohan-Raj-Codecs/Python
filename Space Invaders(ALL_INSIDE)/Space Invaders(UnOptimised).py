import pygame as pg
from pygame import mixer
import random as rn
import time as t

#Re-Organize Code if competed (Bullet Doesn't Need X Coordinates!)

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

#Player
playerImg=pg.image.load('ship.png')
playerX = 370
playerY = 480
player_X_change=0
player_Y_change=0

#Enemy
EnemyImg=[]
EnemyX =[]
EnemyY =[] 
Enemy_X_change=[]
Enemy_Y_change=[]
no_of_Enemy=6

for i in range(no_of_Enemy):
    EnemyImg.append(pg.image.load('enemy.png'))
    EnemyX.append(rn.randint(20,736))
    EnemyY.append(rn.randint(50,200))
    Enemy_X_change.append(0.3)
    Enemy_Y_change.append(40)



#Bullet
BulletImg=pg.image.load('bullet.png')
BulletX = -30  #initially Bullet is at outer space
BulletY = -30  #initially Bullet is at outer space
Bullet_X_change=0
Bullet_Y_change=0
Bullet_state="ready"

#Burst Anime
BurstImg1=pg.image.load('burst hollow.png')
BurstX=30
BurstY=30

#Sounds
mixer.music.load('bg_music.mp3')   #BG Music
mixer.music.play(-1)               #BG Music Playing Infinity
Bullet_Sound=mixer.Sound('shoot.wav')
Explode_Sound=mixer.Sound('explosion.wav')

#Others
isCollide=False
Collide_Type=""
Collide_Pt=0.0
Score_Value=0
font=pg.font.Font('freesansbold.ttf',22)
Game_Over_font=pg.font.Font('freesansbold.ttf',60)
Score_X=10
Score_Y=10
pause=False


def Player(playerX,playerY):  #Marking Player 
    screen.blit(playerImg,(playerX,playerY))

def Enemy(EnemyX,EnemyY,i):  #Marking Enemy
    screen.blit(EnemyImg[i],(EnemyX[i],EnemyY[i]))

def Bullet(x,y):
    screen.blit(BulletImg,(x+24.5,y))  #Bullet from the spaceship

def Burst_Anime(x,y):
    screen.blit(BurstImg1,(x,y))  #Marking Burst Area
        
    
def Show_Score(x,y): #Marking Score
    Score=font.render("Score : "+str(Score_Value),True,(255,255,255))
    screen.blit(Score,(x,y))

def Game_Over(x=250,y=250,Msg="Game Over"):
    Over=Game_Over_font.render(str(Msg),True,(255,255,255))
    screen.blit(Over,(x,y))
    
def Player_Move(x,y,xc,yc): #Moving Player
    x+=xc
    y+=yc
    if x>736:
        x=736
    if x<0:
        x=0
    if y>536:
        y=536
    if y<0:
        y=0
    return x,y,xc,yc

def Enemy_Move(x,y,xc,yc):  #Moving Enemy
    if x <= 0:
        xc=0.3
        y+=yc
    if x >= 736:
        xc=-0.3
        y+=yc
    if x>800 or y>600 :  
        x,y=300,300
    if x<-20 or y<-20:
        x,y=400,200
    x+=xc
    return x,y,xc,yc

def Bullet_Move(x,y,xc,yc):  #Moving Bullet
    global Bullet_state
    global Bullet_Y_change
    if y<-30:
        Bullet_state="ready"
        y=-30
        x=-30
    if Bullet_state=="fire":
        y-=yc
    return x,y,xc,yc
    
def Collision_Detect(px,py,ax,ay,bx,by):
    #Collision Theory  (Max Trautz)  :)   Distance between two points
    ##
    C_type=""
    is_Coll=False
    Coll_Pt=0.0
    ##
    Bullet_Enemy_Collide = ( (ax-bx)**2 + (ay-by)**2 )**0.5
    Player_Enemy_Collide = ( (ax-px)**2 + (ay-py)**2 )**0.5
    if Bullet_Enemy_Collide<27:
        C_type,is_Coll,Coll_Pt="Enemy_Bullet",True,Bullet_Enemy_Collide
    elif Player_Enemy_Collide<45:
        C_type,is_Coll,Coll_Pt="Enemy_Player",True,Player_Enemy_Collide
    if C_type=="Enemy_Bullet":            #burst Anime
        Burst_Anime(ax+Coll_Pt,ay+Coll_Pt)  #burst Anime
        Explode_Sound.play()                   #Explosion Sound Effects
    return C_type,is_Coll,Coll_Pt



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
                pause = not pause
            if event.key == pg.K_LEFT and (not pause): #Detect KEY Left
                player_X_change-=0.7
            if event.key == pg.K_RIGHT and (not pause): #Detect KEY Right
                player_X_change+=0.7
            if event.key == pg.K_UP and (not pause): #Detect KEY Up
                player_Y_change-=0.5
            if event.key == pg.K_DOWN and (not pause): #Detect KEY Down
                player_Y_change+=0.5
            if event.key == pg.K_SPACE and (not pause): #Detect KEY Down
                if Bullet_state=="ready":
                    Bullet(playerX,playerY)
                    BulletX=playerX
                    BulletY=playerY
                    Bullet_Y_change=0.7
                    Bullet_state="fire"
                    Bullet_Sound.play()
        if event.type == pg.KEYUP:  #Detect KEY Release
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN:
                player_X_change=0
                player_Y_change=0
    if pause:
        continue
    
    playerX,playerY,player_X_change,player_Y_change=Player_Move(playerX,playerY,player_X_change,player_Y_change) #Player Recordinate Algo
    for i in range(no_of_Enemy):
        EnemyX[i],EnemyY[i],Enemy_X_change[i],Enemy_Y_change[i]=Enemy_Move(EnemyX[i],EnemyY[i],Enemy_X_change[i],Enemy_Y_change[i])  #Enemy Recordinate Algo
    BulletX,BulletY,Bullet_X_change,Bullet_Y_change=Bullet_Move(BulletX,BulletY,Bullet_X_change,Bullet_Y_change) #Bullet Recordinate Algo
        
    
    Player(playerX,playerY)  #Showing Player with boundary
    Bullet(BulletX,BulletY)  #Showing Bullet with Auto-Dejection(out of space)
    for i in range(no_of_Enemy):
        Enemy(EnemyX,EnemyY,i)     #Showing Enemy with boundary
        Collide_Type,isCollide,Collide_Pt=Collision_Detect(playerX,playerY,EnemyX[i],EnemyY[i],BulletX,BulletY)  #Collision Detect(#Distance between two points)
        if isCollide:
            if Collide_Type=="Enemy_Bullet":
                Score_Value+=1
                BulletY=-30
                Bullet_state="ready"
                EnemyX[i] = rn.randint(0,800)
                EnemyY[i] = rn.randint(50,200)
            elif Collide_Type=="Enemy_Player":    #Terminate Game on Crash
                Explode_Sound.play()
                mixer.music.pause()
                Game_Over()
                Game_Over(275,350,"Score : "+str(Score_Value))
                running=False
    Show_Score(Score_X,Score_Y)  #Display Scores
    
    pg.display.update()              # Updating Coordinates

t.sleep(5)
exit()
    
    
