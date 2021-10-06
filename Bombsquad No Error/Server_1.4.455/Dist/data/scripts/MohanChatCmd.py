import bs
import bsInternal
import os
import bsUtils
import random
import bsSpaz
import copy
import bsMap
import math
import bsCoopGame
import time
import bsAchievement
import weakref
import bsServerData
import threading
import bsGame
import bsUI
import getPermissionsHashes as gph


def Getpb(x):
    x=int(x)
    try:
        for i in bsInternal._getForegroundHostSession().players:
            if i.getInputDevice().getClientID() == x:
                client_pb = i.get_account_id()
    except:
        client_pb="Error"
    return str(client_pb)

            
def Get(x,y):
    cl='clientID'
    fi='displayString'
    po='id'
    pl='players'
    na='name'
    found=False
    x=str(x)
    y=str(y)
    for client in bsInternal._getGameRoster():  
        ser=client[pl]
        for q in ser:     
            ido=str(q[po]) #ID to Any
    #client will be like {'displayString':'\xee\x80\xb0PC284968','specString':'{"n":"PC284968","a":"Local","sn":""}','clientID':-1,'players':[{'namefull':'\xee\x80\xb0PC284968','name':'PC284968','id':0}]}
            if x==ido :
                found=True
            ido=str(client[cl])  #Client to Any
            if x==ido :
                found=True       #Name to Any
            ido=str(q[na])
            if x==ido :
                found=True
            ido=str(client[fi])  #GID to Any
            if x==ido :
                found=True
            ido=str(client[fi])  #GID cut to Any
            ido=str(ido[1:])
            ido=str(ido[1:])
            ido=str(ido[1:])
            if x==ido :
                found=True
            ido=str(Getpb(client[cl]))  #PB to Any
            if x==ido :
                found=True
                
            if found:
                if y=='NAME':
                    return str(q[na])
                if y=='CLID':
                    return str(client[cl])
                if y=='PB':
                    return str(Getpb(client[cl]))
                if y=='ID':
                    return str(q[po])
                if y=='GID':
                    return str(client[fi])
            
    return "Error"

def chk(z):
    x=Getpb(z)
    #lio=[vipHashes,adminHashes,owners,killers,killere,killerq]
    for io in gph.ownerHashes :
        if io == x :
            return True
        else :
            pass
    for io in gph.adminHashes :
        if io == x :
            return True
        else :
            pass
    for io in gph.vipHashes :
        if io == x :
            return True
        else :
            pass
    return False
    
def filt(x,mode='nor'):
    y=x
    x=Getpb(x)

    if mode=='ban' :
        if x in gph.cmd_ban :
            bs.screenMessage('You are Blocked from using Chat Commands', color=(1,0,0), clients=[y], transient=True)
            bs.screenMessage("You are Unable to Use Commands ", color=(1,0,0), clients=[y], transient=True)
            bs.screenMessage("You Misused Our Commands", color=(1,0,0), clients=[y], transient=True)
            return msg
            
    elif mode=='own':
        if x in gph.ownerHashes :
            pass
        else :
            bs.screenMessage('Only Owners can Use This Stuff', color=(1,0,0), clients=[y], transient=True)
            return msg
        
    else :
        if x in gph.cmd_ban :
            bs.screenMessage('You are Blocked from using Chat Commands', color=(1,0,0), clients=[y], transient=True)
            bs.screenMessage("You are Unable to Use Commands ",color=(1,0,0), clients=[y], transient=True)
            bs.screenMessage("You Misused Our Commands",color=(1,0,0), clients=[y], transient=True)
            return msg

        elif chk(y):
            pass
    
        else :
            bs.screenMessage('SOME OF YOU GUYS MISUSED OUR COMMANDS SO COMMANDS DISABLED AND LIMITED', color=(1,0,0), clients=[y], transient=True)
            bs.screenMessage('Use /request        to request Server for Adminship', color=(1,0,0), clients=[y], transient=True)
            bs.screenMessage('Only Admins Can Use Commands', color=(1,0,0), clients=[y], transient=True)
            bsInternal._chatMessage("Only Admins Can Use This Stuff")
            return msg
    
def filterchat(msg,clientID):
    if msg == '/help':
        if chk(clientID):
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("==|No|==|_Official_Command_|=======|_____________________Use_______________|====")
            bsInternal._chatMessage("  |1.|  | /list            |       | List the Players and their ID         | ")
            bsInternal._chatMessage("  |2.|  | /help            |       | To know the commands list applicable  | ")
            bsInternal._chatMessage("  |3.|  | /nv              |       | Turns on the night mode               | ")
            bsInternal._chatMessage("  |4.|  | /nvoff           |       | Turns off the night mode              | ")
            bsInternal._chatMessage("  |6.|  | /camera          |       | This will change the camera view      | ")
            bsInternal._chatMessage("  |7.|  | /sm              |       | Epic Mode                             | ")
            bsInternal._chatMessage("  |8.|  | /end             |       | Ends Current Game                     | ")
            bsInternal._chatMessage("  |9.|  | /remove <ID>     |       | Removes Player for one single game    | ")
            bsInternal._chatMessage("  |10|  | /gm <ID>         |       | God Mode with Extra Powerups          | ")
            bsInternal._chatMessage("  |11|  | /gmall           |       | God Mode for all                      | ")
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("==|No|==|____Fun_Command___|=======|_____________________Use_______________|=")
            bsInternal._chatMessage("  |1.|  | /curse <ID>      |       | Curse the specified Player            | ")
            bsInternal._chatMessage("  |2.|  | /curseall        |       | Curse all the Players                 | ")
            bsInternal._chatMessage("  |3.|  | /kill <ID>       |       | Kill the specified Player             | ")
            bsInternal._chatMessage("  |4.|  | /killall         |       | Kill all the Players                  | ")
            bsInternal._chatMessage("  |5.|  | /freeze <ID>     |       | Freeze the specified Player           | ")
            bsInternal._chatMessage("  |6.|  | /freezeall       |       | Freeze all the Players                | ")
            bsInternal._chatMessage("  |7.|  | /thaw <ID>       |       | UnFreeze the specified Player         | ")
            bsInternal._chatMessage("  |8.|  | /thawall         |       | UnFreeze all the Players              | ")
            bsInternal._chatMessage("  |9.|  | /heal <ID>       |       | Heal the specified Player             | ")
            bsInternal._chatMessage("  |10|  | /healall         |       | Heal all the Players                  | ")
            bsInternal._chatMessage("  |11|  | /headless <ID>   |       | Removes Head the from specified Player| ")
            bsInternal._chatMessage("  |12|  | /headlessall     |       | Removes Head from all the Players     | ")
            bsInternal._chatMessage("  |13|  | /shield <ID>     |       | Gives Shield to the specified Player  | ")
            bsInternal._chatMessage("  |14|  | /shieldall       |       | Gives Shield to all the Players       | ")
            bsInternal._chatMessage("  |15|  | /punch <ID>      |       | Gives Gloves to the specified Player  | ")
            bsInternal._chatMessage("  |16|  | /punchall        |       | Gives Gloves to all the Players       | ")
            bsInternal._chatMessage("  |17|  | /knock <ID>      |       | Gives Knocks to the specified Player  | ")
            bsInternal._chatMessage("  |18|  | /knockall        |       | Gives Knocks to all the Players       | ")
            bsInternal._chatMessage("  |19|  | /celebrate <ID>  |       | The specified Player Celebrates       | ")
            bsInternal._chatMessage("  |20|  | /celebrateall    |       | All Players will Celebrate            | ")
            bsInternal._chatMessage("  |21|  | /hug <ID> <ID>   |       | Two Players will Hug                  | ")
            bsInternal._chatMessage("  |22|  | /hugall          |       | All Players will Hug                  | ")
            bsInternal._chatMessage("  |23|  | /secret <ID>     |       | You will be Super Mario               | ")
            bsInternal._chatMessage("  |24|  | /secretall       |       | All Will be Super Mario               | ")
            bsInternal._chatMessage("  |25|  | /model           |       | All Models will be Displayed          | ")
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("  |1.|  | /kick            |       | This will kick players                | ")
        else:
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("==|No|==|_Official_Command_|=======|_____________________Use_______________|====")
            bsInternal._chatMessage("  |1.|  | /list            |       | List the Players and their ID         | ")
            bsInternal._chatMessage("  |2.|  | /help            |       | To know the commands list applicable  | ")
            bsInternal._chatMessage("  |3.|  | /nv              |       | Turns on the night mode               | ")
            bsInternal._chatMessage("  |4.|  | /nvoff           |       | Turns off the night mode              | ")
            bsInternal._chatMessage("  |5.|  | /sm              |       | Epic Mode                             | ")
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("==|No|==|____Fun_Command___|=======|_____________________Use_______________|=")
            bsInternal._chatMessage("  |1.|  | /gmall           |       | God Mode for all                      | ")
            bsInternal._chatMessage("  |2.|  | /curseall        |       | Curse all the Players                 | ")
            bsInternal._chatMessage("  |3.|  | /freezeall       |       | Freeze all the Players                | ")
            bsInternal._chatMessage("  |4.|  | /thawall         |       | UnFreeze all the Players              | ")
            bsInternal._chatMessage("  |5.|  | /healall         |       | Heal all the Players                  | ")
            bsInternal._chatMessage("  |6.|  | /headlessall     |       | Removes Head from all the Players     | ")
            bsInternal._chatMessage("  |7.|  | /shieldall       |       | Gives Shield to all the Players       | ")
            bsInternal._chatMessage("  |8.|  | /punchall        |       | Gives Gloves to all the Players       | ")
            bsInternal._chatMessage("  |9.|  | /knockall        |       | Gives Knocks to all the Players       | ")
            bsInternal._chatMessage("  |10|  | /celebrateall    |       | All Players will Celebrate            | ")
            bsInternal._chatMessage("  |11|  | /hugall          |       | All Players will Hug                  | ")
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("SOME OF YOU GUYS MISUSED OUR COMMANDS SO COMMANDS DISABLED AND LIMITED")
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
            bsInternal._chatMessage("  |1.|  | /request         |       | Requests Your Server for Adminship    | ")
            bsInternal._chatMessage("---------------------------------------------------------------------------| ")
        
    #
    mem=0
    m = msg.split(' ',1)[0] # command
    a = msg.split(' ')[1:]
    activity = bsInternal._getForegroundHostActivity()
    #
    with bs.Context(activity):
        if m == '/get':
            bsInternal._chatMessage(Get(str(a[0]),str(a[1])))

        elif m == '/pb':
            bs.screenMessage('Pb ID : '+(Getpb(clientID)), color=(1,0,0), clients=[clientID], transient=True)
            
        elif m == '/list':
            bsInternal._chatMessage("/help for commands list")
            bsInternal._chatMessage("======= Listing Players =======")
            bsInternal._chatMessage("=|No.|==|Name|===========|ID|==|ClientID|==")
            for s in bsInternal._getGameRoster():
                pla=s['players']
                for iq in pla:
                    ide=str(iq['id'])
                hw=0
                spacer=''
                mem+=1
                na=Get(ide,'NAME')#17#11#
                hw=len(na)
                spac=27-hw
                for qo in range(0,spac-2):
                    spacer+=' '
                if hw > 10 :
                    spacer='       '
                bsInternal._chatMessage("   |"+str(mem)+".|      |"+ na +'|'+spacer+'|'+ide+'|      '+'|   '+Get(ide,'CLID')+'   |')
                
        elif m == '/nv':
            filt(clientID,mode='ban')
            bs.getSharedObject('globals').tint = (0.5,0.7,1)

        elif m == '/nvoff' :
            filt(clientID,mode='ban')
            bs.getSharedObject('globals').tint = (1.20,1.17,1.10)

        elif m == '/kick': #just remove from the game
         #   bs.screenMessage("/kick is removed for some reasons", color=(1,0,0), clients=[clientID], transient=True)
         #   bsInternal._chatMessage("/kick is removed for some reasons")
          #  bsInternal._chatMessage("Because Players kick each other and Hurts Them")
           # bsInternal._chatMessage("It will be added soon with security flow")
            filt(clientID)
            if a == []:
                bs.screenMessage('MUST USE KICK ID', color=(1,0,0), clients=[clientID], transient=True)
                bsInternal._chatMessage("==========PLAYER KICK IDS==========")
                for i in bsInternal._getGameRoster():
                    bsInternal._chatMessage('  |Name|= '+i['players'][0]['nameFull'] + "    |kick ID|= " + str(i['clientID']))
            else:
                if Get(a,'PB') in gph.ownersHashes :
                    bsInternal._chatMessage(' Cannot Kick Owners :( ')
                    return msg
                try:
                    kickedPlayerID = int(a[0])
                except Exception:
                    bs.screenMessage('PLAYER NOT FOUND', color=(1,0,0), clients=[clientID], transient=True)
                else:
                    if not kickedPlayerID == -1:
                        bsInternal._disconnectClient(kickedPlayerID)
                        bsInternal._chatMessage('Kicked '+str(kickedPlayerID))
                    else:
                        bs.screenMessage('CANT KICK HOST', color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/camera': #change camera mode
            filt(clientID)
            try:
                if bs.getSharedObject('globals').cameraMode == 'follow':
                    bsInternal._chatMessage('Rotate Camera Mode')
                    bs.getSharedObject('globals').cameraMode = 'rotate'
                else:
                    bs.getSharedObject('globals').cameraMode = 'follow'
                    bsInternal._chatMessage('Follow Camera mode')
            except Exception:
                bs.screenMessage("AN ERROR OCCURED", color=(1,0,0), clients=[clientID], transient=True)
                
        elif m == '/curse': #curse
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.curse()
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.curse()
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/curseall' or '/curse all': #curse all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.curse()
                except Exception:
                    pass

        elif m == '/kill': #kill
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.DieMessage())
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.DieMessage())
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/killall' or '/kill all': #kill all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.DieMessage())
                except Exception:
                    pass
                     
        elif m == '/freeze': #freeze
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.FreezeMessage())
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.FreezeMessage())
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/freezeall' or '/freeze all': #freeze all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.FreezeMessage())
                except Exception:
                    pass

        elif m == '/heal': #heal
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'health'))
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'health'))
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                            
        elif m == '/healall' or '/heal all': #heal all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'health'))
                except Exception:
                    pass

        elif m == '/secret': #smario
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'smario'))
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'smario'))
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                            
        elif m == '/secretall' or '/secret all': #smario all
            filt(clientID)
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'smario'))
                except Exception:
                    pass        

        elif m == '/thaw': #thaw
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.ThawMessage())
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.ThawMessage())
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                
        elif m == '/thawall' or '/thaw all': #thaw all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.ThawMessage())
                except Exception:
                    pass
        
                
        elif m == '/headless': #headless
            filt(clientID,mode='ban')
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = None
                                    i.actor.node.style = "cyborg"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel = None
                        bs.getActivity().players[int(a[0])].actor.node.style = "cyborg"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/headlessall' or '/headless all': #headless all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = None
                        i.actor.node.style = "cyborg"
                except Exception:
                        pass
                
        elif m == '/shield': #shield
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'shield'))
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'shield'))
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/shieldall' or '/shield all': #shield all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'shield'))
                except Exception:
                    pass
                        
        elif m == '/punch': #punch
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                
        elif m == '/punchall' or '/punch all': #punch all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
                except Exception:
                    pass
                
        elif m == '/knock': #knock him
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage("knockout",5000)
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage("knockout",5000)
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                            
        elif m == '/knockall' or '/knock all': #knock all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage("knockout",5000)
                except Exception:
                    pass
                
        elif m == '/celebrate': #celebrate him
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage('celebrate', 30000)
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage('celebrate', 30000)
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/celebrateall' or '/celebrate all': #celebrate all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.handleMessage('celebrate', 30000)
                except Exception:
                    pass
                
        elif m == '/sm': # slow-mo
            try:
                if bs.getSharedObject('globals').slowMotion == True:
                    bs.getSharedObject('globals').slowMotion = False
                else:
                    bs.getSharedObject('globals').slowMotion = True
            except Exception:
                bs.screenMessage("AN ERROR OCCURED", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/end': # just finish the game
            filt(clientID)
            try:
                bsInternal._getForegroundHostActivity().endGame()
                bsInternal._chatMessage('THE END')
            except Exception:
                bs.screenMessage("AN ERROR OCCURED", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/remove': #remove from game
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                i.removeFromGame()
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].removeFromGame()
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/gm': #shield
            filt(clientID)
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
                                    i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'speedy'))
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'speedy'))
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/gmall' or '/gm all': #shield all
                filt(clientID,mode='ban')
                for i in bs.getActivity().players:
                    try:
                        if i.actor.exists():
                            i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
                            i.actor.node.handleMessage(bs.PowerupMessage(powerupType = 'speedy'))
                    except Exception:
                            pass
                        
        elif m == '/invisible': #headless
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = None
                                    i.actor.node.torsoModel = None
                                    i.actor.node.pelvisModel = None
                                    i.actor.node.upperArmModel = None
                                    i.actor.node.foreArmModel = None
                                    i.actor.node.handModel = None
                                    i.actor.node.upperLegModel = None
                                    i.actor.node.lowerLegModel = None
                                    i.actor.node.toesModel = None
                                    i.actor.node.style = None
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel = None
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = None
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = None
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = None
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = None
                        bs.getActivity().players[int(a[0])].actor.node.handModel = None
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = None
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = None
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = None
                        bs.getActivity().players[int(a[0])].actor.node.style = None
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)
                                 
        elif m == '/invisibleall' or '/invisible all': #headless all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = None
                        i.actor.node.torsoModel = None
                        i.actor.node.pelvisModel = None
                        i.actor.node.upperArmModel = None
                        i.actor.node.foreArmModel = None
                        i.actor.node.handModel = None
                        i.actor.node.upperLegModel = None
                        i.actor.node.lowerLegModel = None
                        i.actor.node.toesModel = None
                        i.actor.node.style = None
                except Exception:
                    pass
        elif m == '/model' : #Models
            models=['kronk','zoe','jack','mel','ninja','bunny','bones','bear','agent','frosty','penguin','pixie','wizard','santa','alien']
            for i in models :
                model=str('| /'+i+' | '+'Change '+i+' as your Appearence |')
                bsInternal._chatMessage(model)

        elif m == '/kronk': #kronk
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("kronkHead")
                                    i.actor.node.torsoModel = bs.getModel("kronkTorso")
                                    i.actor.node.pelvisModel = bs.getModel("kronkPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("kronkUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("kronkForeArm")
                                    i.actor.node.handModel = bs.getModel("kronkHand")
                                    i.actor.node.upperLegModel = bs.getModel("kronkUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("kronkLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("kronkToes")
                                    i.actor.node.style = "kronk"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("kronkHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("kronkTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("kronkPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("kronkUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("kronkForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("kronkHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("kronkUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("kronkLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("kronkToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "kronk"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/kronkall' or '/kronk all': #kronk all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("kronkHead")
                        i.actor.node.torsoModel = bs.getModel("kronkTorso")
                        i.actor.node.pelvisModel = bs.getModel("kronkPelvis")
                        i.actor.node.upperArmModel = bs.getModel("kronkUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("kronkForeArm")
                        i.actor.node.handModel = bs.getModel("kronkHand")
                        i.actor.node.upperLegModel = bs.getModel("kronkUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("kronkLowerLeg")
                        i.actor.node.toesModel = bs.getModel("kronkToes")
                        i.actor.node.style = "kronk"
                except Exception:
                    pass

        elif m == '/zoe': #zoe
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("zoeHead")
                                    i.actor.node.torsoModel = bs.getModel("zoeTorso")
                                    i.actor.node.pelvisModel = bs.getModel("zoePelvis")
                                    i.actor.node.upperArmModel = bs.getModel("zoeUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("zoeForeArm")
                                    i.actor.node.handModel = bs.getModel("zoeHand")
                                    i.actor.node.upperLegModel = bs.getModel("zoeUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("zoeLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("zoeToes")
                                    i.actor.node.style = "female"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("zoeHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("zoeTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("zoePelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("zoeUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("zoeForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("zoeHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("zoeUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("zoeLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("zoeToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "female"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/zoeall' or '/zoe all': #zoe all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("zoeHead")
                        i.actor.node.torsoModel = bs.getModel("zoeTorso")
                        i.actor.node.pelvisModel = bs.getModel("zoePelvis")
                        i.actor.node.upperArmModel = bs.getModel("zoeUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("zoeForeArm")
                        i.actor.node.handModel = bs.getModel("zoeHand")
                        i.actor.node.upperLegModel = bs.getModel("zoeUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("zoeLowerLeg")
                        i.actor.node.toesModel = bs.getModel("zoeToes")
                        i.actor.node.style = "female"
                except Exception:
                    pass

        elif m == '/jack': #jack
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("jackHead")
                                    i.actor.node.torsoModel = bs.getModel("jackTorso")
                                    i.actor.node.pelvisModel = bs.getModel("kronkPelvis")    #Note : This is Correct that this character uses kronk pelvis
                                    i.actor.node.upperArmModel = bs.getModel("jackUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("jackForeArm")
                                    i.actor.node.handModel = bs.getModel("jackHand")
                                    i.actor.node.upperLegModel = bs.getModel("jackUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("jackLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("jackToes")
                                    i.actor.node.style = "pirate"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("jackHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("jackTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("kronkPelvis")    #Note : This is Correct that this character uses kronk pelvis
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("jackUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("jackForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("jackHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("jackUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("jackLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("jackToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "pirate"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/jackall' or '/jack all': #jack all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("jackHead")
                        i.actor.node.torsoModel = bs.getModel("jackTorso")
                        i.actor.node.pelvisModel = bs.getModel("kronkPelvis")    #Note : This is Correct that this character uses kronk pelvis
                        i.actor.node.upperArmModel = bs.getModel("jackUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("jackForeArm")
                        i.actor.node.handModel = bs.getModel("jackHand")
                        i.actor.node.upperLegModel = bs.getModel("jackUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("jackLowerLeg")
                        i.actor.node.toesModel = bs.getModel("jackToes")
                        i.actor.node.style = "pirate"
                except Exception:
                    pass

        elif m == '/mel': #mel
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("melHead")
                                    i.actor.node.torsoModel = bs.getModel("melTorso")
                                    i.actor.node.pelvisModel = bs.getModel("kronkPelvis")   #Note : This is Correct that this character uses kronk pelvis
                                    i.actor.node.upperArmModel = bs.getModel("melUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("melForeArm")
                                    i.actor.node.handModel = bs.getModel("melHand")
                                    i.actor.node.upperLegModel = bs.getModel("melUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("melLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("melToes")
                                    i.actor.node.style = "mel"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("melHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("melTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("kronkPelvis")    #Note : This is Correct that this character uses kronk pelvis
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("melUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("melForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("melHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("melUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("melLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("melToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "mel"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/melall' or '/mel all': #mel all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("melHead")
                        i.actor.node.torsoModel = bs.getModel("melTorso")
                        i.actor.node.pelvisModel = bs.getModel("kronkPelvis")    #Note : This is Correct that this character uses kronk pelvis
                        i.actor.node.upperArmModel = bs.getModel("melUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("melForeArm")
                        i.actor.node.handModel = bs.getModel("melHand")
                        i.actor.node.upperLegModel = bs.getModel("melUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("melLowerLeg")
                        i.actor.node.toesModel = bs.getModel("melToes")
                        i.actor.node.style = "mel"
                except Exception:
                    pass
					
        elif m == '/ninja': #ninja
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("ninjaHead")
                                    i.actor.node.torsoModel = bs.getModel("ninjaTorso")
                                    i.actor.node.pelvisModel = bs.getModel("ninjaPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("ninjaUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("ninjaForeArm")
                                    i.actor.node.handModel = bs.getModel("ninjaHand")
                                    i.actor.node.upperLegModel = bs.getModel("ninjaUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("ninjaLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("ninjaToes")
                                    i.actor.node.style = "ninja"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("ninjaHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("ninjaTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("ninjaPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("ninjaUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("ninjaForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("ninjaHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("ninjaUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("ninjaLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("ninjaToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "ninja"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/ninjaall' or '/ninja all': #ninja all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("ninjaHead")
                        i.actor.node.torsoModel = bs.getModel("ninjaTorso")
                        i.actor.node.pelvisModel = bs.getModel("ninjaPelvis")
                        i.actor.node.upperArmModel = bs.getModel("ninjaUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("ninjaForeArm")
                        i.actor.node.handModel = bs.getModel("ninjaHand")
                        i.actor.node.upperLegModel = bs.getModel("ninjaUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("ninjaLowerLeg")
                        i.actor.node.toesModel = bs.getModel("ninjaToes")
                        i.actor.node.style = "ninja"
                except Exception:
                    pass

        elif m == '/bunny': #bunny
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("bunnyHead")
                                    i.actor.node.torsoModel = bs.getModel("bunnyTorso")
                                    i.actor.node.pelvisModel = bs.getModel("bunnyPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("bunnyUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("bunnyForeArm")
                                    i.actor.node.handModel = bs.getModel("bunnyHand")
                                    i.actor.node.upperLegModel = bs.getModel("bunnyUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("bunnyLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("bunnyToes")
                                    i.actor.node.style = "bunny"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("bunnyHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("bunnyTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("bunnyPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("bunnyUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("bunnyForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("bunnyHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("bunnyUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("bunnyLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("bunnyToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "bunny"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/bunnyall' or '/bunny all': #bunny all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("bunnyHead")
                        i.actor.node.torsoModel = bs.getModel("bunnyTorso")
                        i.actor.node.pelvisModel = bs.getModel("bunnyPelvis")
                        i.actor.node.upperArmModel = bs.getModel("bunnyUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("bunnyForeArm")
                        i.actor.node.handModel = bs.getModel("bunnyHand")
                        i.actor.node.upperLegModel = bs.getModel("bunnyUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("bunnyLowerLeg")
                        i.actor.node.toesModel = bs.getModel("bunnyToes")
                        i.actor.node.style = "bunny"
                except Exception:
                    pass
						
        elif m == '/bones': #bones
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("bonesHead")
                                    i.actor.node.torsoModel = bs.getModel("bonesTorso")
                                    i.actor.node.pelvisModel = bs.getModel("bonesPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("bonesUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("bonesForeArm")
                                    i.actor.node.handModel = bs.getModel("bonesHand")
                                    i.actor.node.upperLegModel = bs.getModel("bonesUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("bonesLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("bonesToes")
                                    i.actor.node.style = "bones"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("bonesHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("bonesTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("bonesPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("bonesUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("bonesForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("bonesHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("bonesUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("bonesLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("bonesToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "bones"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/bonesall' or '/bones all': #bones all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("bonesHead")
                        i.actor.node.torsoModel = bs.getModel("bonesTorso")
                        i.actor.node.pelvisModel = bs.getModel("bonesPelvis")
                        i.actor.node.upperArmModel = bs.getModel("bonesUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("bonesForeArm")
                        i.actor.node.handModel = bs.getModel("bonesHand")
                        i.actor.node.upperLegModel = bs.getModel("bonesUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("bonesLowerLeg")
                        i.actor.node.toesModel = bs.getModel("bonesToes")
                        i.actor.node.style = "bones"
                except Exception:
                    pass
					

        elif m == '/bear': #bear
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("bearHead")
                                    i.actor.node.torsoModel = bs.getModel("bearTorso")
                                    i.actor.node.pelvisModel = bs.getModel("bearPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("bearUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("bearForeArm")
                                    i.actor.node.handModel = bs.getModel("bearHand")
                                    i.actor.node.upperLegModel = bs.getModel("bearUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("bearLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("bearToes")
                                    i.actor.node.style = "bear"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("bearHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("bearTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("bearPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("bearUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("bearForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("bearHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("bearUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("bearLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("bearToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "bear"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/bearall' or '/bear all': #bear all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("bearHead")
                        i.actor.node.torsoModel = bs.getModel("bearTorso")
                        i.actor.node.pelvisModel = bs.getModel("bearPelvis")
                        i.actor.node.upperArmModel = bs.getModel("bearUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("bearForeArm")
                        i.actor.node.handModel = bs.getModel("bearHand")
                        i.actor.node.upperLegModel = bs.getModel("bearUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("bearLowerLeg")
                        i.actor.node.toesModel = bs.getModel("bearToes")
                        i.actor.node.style = "bear"
                except Exception:
                    pass
					
        elif m == '/agent': #agent
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("agentHead")
                                    i.actor.node.torsoModel = bs.getModel("agentTorso")
                                    i.actor.node.pelvisModel = bs.getModel("agentPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("agentUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("agentForeArm")
                                    i.actor.node.handModel = bs.getModel("agentHand")
                                    i.actor.node.upperLegModel = bs.getModel("agentUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("agentLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("agentToes")
                                    i.actor.node.style = "agent"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("agentHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("agentTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("agentPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("agentUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("agentForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("agentHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("agentUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("agentLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("agentToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "agent"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/agentall' or '/agent all': #agent all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("agentHead")
                        i.actor.node.torsoModel = bs.getModel("agentTorso")
                        i.actor.node.pelvisModel = bs.getModel("agentPelvis")
                        i.actor.node.upperArmModel = bs.getModel("agentUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("agentForeArm")
                        i.actor.node.handModel = bs.getModel("agentHand")
                        i.actor.node.upperLegModel = bs.getModel("agentUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("agentLowerLeg")
                        i.actor.node.toesModel = bs.getModel("agentToes")
                        i.actor.node.style = "agent"
                except Exception:
                    pass
					
        elif m == '/frosty': #frosty
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("frostyHead")
                                    i.actor.node.torsoModel = bs.getModel("frostyTorso")
                                    i.actor.node.pelvisModel = bs.getModel("frostyPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("frostyUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("frostyForeArm")
                                    i.actor.node.handModel = bs.getModel("frostyHand")
                                    i.actor.node.upperLegModel = bs.getModel("frostyUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("frostyLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("frostyToes")
                                    i.actor.node.style = "frosty"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("frostyHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("frostyTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("frostyPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("frostyUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("frostyForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("frostyHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("frostyUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("frostyLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("frostyToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "frosty"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/frostyall' or '/frosty all': #frosty all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("frostyHead")
                        i.actor.node.torsoModel = bs.getModel("frostyTorso")
                        i.actor.node.pelvisModel = bs.getModel("frostyPelvis")
                        i.actor.node.upperArmModel = bs.getModel("frostyUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("frostyForeArm")
                        i.actor.node.handModel = bs.getModel("frostyHand")
                        i.actor.node.upperLegModel = bs.getModel("frostyUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("frostyLowerLeg")
                        i.actor.node.toesModel = bs.getModel("frostyToes")
                        i.actor.node.style = "frosty"
                except Exception:
                    pass
					
        elif m == '/penguin': #penguin
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("penguinHead")
                                    i.actor.node.torsoModel = bs.getModel("penguinTorso")
                                    i.actor.node.pelvisModel = bs.getModel("penguinPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("penguinUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("penguinForeArm")
                                    i.actor.node.handModel = bs.getModel("penguinHand")
                                    i.actor.node.upperLegModel = bs.getModel("penguinUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("penguinLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("penguinToes")
                                    i.actor.node.style = "penguin"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("penguinHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("penguinTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("penguinPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("penguinUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("penguinForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("penguinHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("penguinUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("penguinLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("penguinToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "penguin"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/penguinall' or '/penguin all': #penguin all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("penguinHead")
                        i.actor.node.torsoModel = bs.getModel("penguinTorso")
                        i.actor.node.pelvisModel = bs.getModel("penguinPelvis")
                        i.actor.node.upperArmModel = bs.getModel("penguinUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("penguinForeArm")
                        i.actor.node.handModel = bs.getModel("penguinHand")
                        i.actor.node.upperLegModel = bs.getModel("penguinUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("penguinLowerLeg")
                        i.actor.node.toesModel = bs.getModel("penguinToes")
                        i.actor.node.style = "penguin"
                except Exception:
                    pass
					
        elif m == '/pixie': #pixie
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("pixieHead")
                                    i.actor.node.torsoModel = bs.getModel("pixieTorso")
                                    i.actor.node.pelvisModel = bs.getModel("pixiePelvis")
                                    i.actor.node.upperArmModel = bs.getModel("pixieUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("pixieForeArm")
                                    i.actor.node.handModel = bs.getModel("pixieHand")
                                    i.actor.node.upperLegModel = bs.getModel("pixieUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("pixieLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("pixieToes")
                                    i.actor.node.style = "pixie"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("pixieHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("pixieTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("pixiePelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("pixieUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("pixieForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("pixieHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("pixieUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("pixieLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("pixieToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "pixie"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/pixieall' or '/pixie all': #pixie all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("pixieHead")
                        i.actor.node.torsoModel = bs.getModel("pixieTorso")
                        i.actor.node.pelvisModel = bs.getModel("pixiePelvis")
                        i.actor.node.upperArmModel = bs.getModel("pixieUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("pixieForeArm")
                        i.actor.node.handModel = bs.getModel("pixieHand")
                        i.actor.node.upperLegModel = bs.getModel("pixieUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("pixieLowerLeg")
                        i.actor.node.toesModel = bs.getModel("pixieToes")
                        i.actor.node.style = "pixie"
                except Exception:
                    pass
					

        elif m == '/wizard': #wizard
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("wizardHead")
                                    i.actor.node.torsoModel = bs.getModel("wizardTorso")
                                    i.actor.node.pelvisModel = bs.getModel("wizardPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("wizardUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("wizardForeArm")
                                    i.actor.node.handModel = bs.getModel("wizardHand")
                                    i.actor.node.upperLegModel = bs.getModel("wizardUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("wizardLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("wizardToes")
                                    i.actor.node.style = "wizard"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("wizardHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("wizardTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("wizardPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("wizardUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("wizardForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("wizardHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("wizardUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("wizardLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("wizardToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "wizard"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/wizardall' or '/wizard all': #wizard all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("wizardHead")
                        i.actor.node.torsoModel = bs.getModel("wizardTorso")
                        i.actor.node.pelvisModel = bs.getModel("wizardPelvis")
                        i.actor.node.upperArmModel = bs.getModel("wizardUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("wizardForeArm")
                        i.actor.node.handModel = bs.getModel("wizardHand")
                        i.actor.node.upperLegModel = bs.getModel("wizardUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("wizardLowerLeg")
                        i.actor.node.toesModel = bs.getModel("wizardToes")
                        i.actor.node.style = "wizard"
                except Exception:
                    pass
					
        elif m == '/cyborg': #cyborg
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("cyborgHead")
                                    i.actor.node.torsoModel = bs.getModel("cyborgTorso")
                                    i.actor.node.pelvisModel = bs.getModel("cyborgPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("cyborgUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("cyborgForeArm")
                                    i.actor.node.handModel = bs.getModel("cyborgHand")
                                    i.actor.node.upperLegModel = bs.getModel("cyborgUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("cyborgLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("cyborgToes")
                                    i.actor.node.style = "cyborg"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("cyborgHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("cyborgTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("cyborgPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("cyborgUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("cyborgForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("cyborgHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("cyborgUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("cyborgLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("cyborgToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "cyborg"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/cyborgall' or '/cyborg all': #cyborg all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("cyborgHead")
                        i.actor.node.torsoModel = bs.getModel("cyborgTorso")
                        i.actor.node.pelvisModel = bs.getModel("cyborgPelvis")
                        i.actor.node.upperArmModel = bs.getModel("cyborgUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("cyborgForeArm")
                        i.actor.node.handModel = bs.getModel("cyborgHand")
                        i.actor.node.upperLegModel = bs.getModel("cyborgUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("cyborgLowerLeg")
                        i.actor.node.toesModel = bs.getModel("cyborgToes")
                        i.actor.node.style = "cyborg"
                except Exception:
                    pass
					
        elif m == '/santa': #santa
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("santaHead")
                                    i.actor.node.torsoModel = bs.getModel("santaTorso")
                                    i.actor.node.pelvisModel = bs.getModel("kronkPelvis")        #Note : This is Correct that this character uses kronk pelvis
                                    i.actor.node.upperArmModel = bs.getModel("santaUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("santaForeArm")
                                    i.actor.node.handModel = bs.getModel("santaHand")
                                    i.actor.node.upperLegModel = bs.getModel("santaUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("santaLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("santaToes")
                                    i.actor.node.style = "santa"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("santaHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("santaTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("kronkPelvis")      #Note : This is Correct that this character uses kronk pelvis
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("santaUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("santaForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("santaHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("santaUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("santaLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("santaToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "santa"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/santaall' or '/santa all': #santa all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("santaHead")
                        i.actor.node.torsoModel = bs.getModel("santaTorso")
                        i.actor.node.pelvisModel = bs.getModel("kronkPelvis")          #Note : This is Correct that this character uses kronk pelvis
                        i.actor.node.upperArmModel = bs.getModel("santaUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("santaForeArm")
                        i.actor.node.handModel = bs.getModel("santaHand")
                        i.actor.node.upperLegModel = bs.getModel("santaUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("santaLowerLeg")
                        i.actor.node.toesModel = bs.getModel("santaToes")
                        i.actor.node.style = "santa"
                except Exception:
                    pass
					

        elif m == '/alien': #alien
            if a == []:
                bs.screenMessage("MUST USE PLAYER ID OR NICK", color=(1,0,0), clients=[clientID], transient=True)
            else:
                filt(clientID)
                if len(a[0]) > 2:
                    for i in bs.getActivity().players:
                        try:
                            if (i.getName()).encode('utf-8') == (a[0]):
                                if i.actor.exists():
                                    i.actor.node.headModel = bs.getModel("alienHead")
                                    i.actor.node.torsoModel = bs.getModel("alienTorso")
                                    i.actor.node.pelvisModel = bs.getModel("alienPelvis")
                                    i.actor.node.upperArmModel = bs.getModel("alienUpperArm")
                                    i.actor.node.foreArmModel = bs.getModel("alienForeArm")
                                    i.actor.node.handModel = bs.getModel("alienHand")
                                    i.actor.node.upperLegModel = bs.getModel("alienUpperLeg")
                                    i.actor.node.lowerLegModel = bs.getModel("alienLowerLeg")
                                    i.actor.node.toesModel = bs.getModel("alienToes")
                                    i.actor.node.style = "alien"
                        except Exception:
                            pass
                else:
                    try:
                        bs.getActivity().players[int(a[0])].actor.node.headModel =  bs.getModel("alienHead")
                        bs.getActivity().players[int(a[0])].actor.node.torsoModel = bs.getModel("alienTorso")
                        bs.getActivity().players[int(a[0])].actor.node.pelvisModel = bs.getModel("alienPelvis")
                        bs.getActivity().players[int(a[0])].actor.node.upperArmModel = bs.getModel("alienUpperArm")
                        bs.getActivity().players[int(a[0])].actor.node.foreArmModel = bs.getModel("alienForeArm")
                        bs.getActivity().players[int(a[0])].actor.node.handModel = bs.getModel("alienHand")
                        bs.getActivity().players[int(a[0])].actor.node.upperLegModel = bs.getModel("alienUpperLeg")
                        bs.getActivity().players[int(a[0])].actor.node.lowerLegModel = bs.getModel("alienLowerLeg")
                        bs.getActivity().players[int(a[0])].actor.node.toesModel = bs.getModel("alienToes")
                        bs.getActivity().players[int(a[0])].actor.node.style = "alien"
                    except Exception:
                        bs.screenMessage("PLAYER NOT FOUND", color=(1,0,0), clients=[clientID], transient=True)

        elif m == '/alienall' or '/alien all': #alien all
            filt(clientID,mode='ban')
            for i in bs.getActivity().players:
                try:
                    if i.actor.exists():
                        i.actor.node.headModel = bs.getModel("alienHead")
                        i.actor.node.torsoModel = bs.getModel("alienTorso")
                        i.actor.node.pelvisModel = bs.getModel("alienPelvis")
                        i.actor.node.upperArmModel = bs.getModel("alienUpperArm")
                        i.actor.node.foreArmModel = bs.getModel("alienForeArm")
                        i.actor.node.handModel = bs.getModel("alienHand")
                        i.actor.node.upperLegModel = bs.getModel("alienUpperLeg")
                        i.actor.node.lowerLegModel = bs.getModel("alienLowerLeg")
                        i.actor.node.toesModel = bs.getModel("alienToes")
                        i.actor.node.style = "alien"
                except Exception:
                    pass

        elif m == '/request' :
            if not chk(clientID):
                bsInternal._chatMessage('Your Request is Submitted')
                with open(bs.getEnvironment()['systemScriptsDirectory'] +"/Rist.txt","a") as fg :
                    fg.write('\n')
                    fg.write(Get(clientID,'GID')+" Requests for admin or Vip <ID> = "+Get(clientID,'PB'))
                fg.close()
                bsInternal._chatMessage('You can Send Multiple Requests')
                bs.screenMessage("Submission Complete", color=(0,1,0), clients=[clientID], transient=True)
            else:
                bs.screenMessage("You are Already a Elevated Person", color=(0,1,0), clients=[clientID], transient=True)
                bsInternal._chatMessage('You are Already a Important person to this SERVER')

        elif m == '/disable':
            if len(a)==0:
                bs.screenMessage("Please Use Player ID     use /list to see ID", color=(1,0,0), clients=[clientID], transient=True)
                bsInternal._chatMessage('Please Use Player ID     use /list to see ID')
            else :
                filt(clientID,mode='own')
                gph.cmd_ban.append(Get(a[0],'PB'))
                bsInternal._chatMessage('Player Disabled Commands')
                bsInternal._chatMessage('Thanks for Improving our Server')
        elif m == '/enable':
            if len(a)==0:
                bs.screenMessage("Please Use Player ID     use /list to see ID", color=(1,0,0), clients=[clientID], transient=True)
                bsInternal._chatMessage('Please Use Player ID     use /list to see ID')
            else :
                filt(clientID,mode='own')
                gph.cmd_ban.remove(Get(a[0],'PB'))
                bsInternal._chatMessage('Player Enabled Commands')
                bsInternal._chatMessage('Thanks for Improving our Server')

        elif m == '/hug' :
            if len(a)==0 :
                bs.screenMessage("Please Use Player ID     use /list to see ID", color=(1,0,0), clients=[clientID], transient=True)

            else :
                filt(clientID)
                bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[int(a[1])].actor.node
                bs.screenMessage("Love Making Lol", color=(1,0.1,1), clients=[clientID], transient=True)
                bs.screenMessage("Spreading Love by Hug", color=(1,0.1,1), clients=[clientID], transient=True)

        elif m == '/hugall' or '/hug all':
            filt(clientID,mode='ban')
            try:
                bsInternal._getForegroundHostActivity().players[0].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[1].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[1].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[2].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[2].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[3].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[3].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[4].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[4].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[5].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[5].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[6].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[6].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[7].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[7].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[8].actor.node
            except:
                pass
            try:
                bsInternal._getForegroundHostActivity().players[8].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[0].actor.node
            except:
                pass
            bs.screenMessage("Love Making Lol", color=(1,0.1,1), clients=[clientID], transient=True)
            bs.screenMessage("Spreading Love by Hug", color=(1,0.1,1), clients=[clientID], transient=True)
        
        elif m == '/admin':
            if len(a)==0:
                bs.screenMessage("Please Use Player ID     use /list to see ID", color=(1,0,0), clients=[clientID], transient=True)
                bsInternal._chatMessage('Please Use Player ID     use /list to see ID')
            else :
                filt(clientID,mode='own')
                gph.adminHashes.append(Get(a[0],'PB'))
                abc=Get(a[0],'NAME')+' is Admin Now'
                bsInternal._chatMessage(abc)
                bs.screenMessage(abc, color=(0,1,0),transient=True)
                
        elif m == '/vip':
            if len(a)==0:
                bs.screenMessage("Please Use Player ID     use /list to see ID", color=(1,0,0), clients=[clientID], transient=True)
                bsInternal._chatMessage('Please Use Player ID     use /list to see ID')
            else :
                filt(clientID,mode='own')
                gph.vipHashes.append(Get(a[0],'PB'))
                abc=Get(a[0],'NAME')+' is VIP Now'
                bsInternal._chatMessage(abc)
                bs.screenMessage(abc, color=(0,1,0),transient=True)

        elif m== '/dismiss':
            if len(a)==0:
                bs.screenMessage("Please Use Player ID     use /list to see ID", color=(1,0,0), clients=[clientID], transient=True)
                bsInternal._chatMessage('Please Use Player ID     use /list to see ID')
            else :
                filt(clientID,mode='own')
                ID=str(Get(a[0],'PB'))
                if ID in gph.adminHashes :
                    gph.adminHashes.remove(ID)
                    abc=Get(a[0],'NAME')+' is Dismissed From Admin post'
                    bsInternal._chatMessage(abc)
                    bs.screenMessage(abc, color=(1,0,0),transient=True)
                if ID in gph.vipHashes :
                    gph.vipHashes.remove(ID)
                    abc=Get(a[0],'NAME')+' is Dismissed From VIP post'
                    bsInternal._chatMessage(abc)
                    bs.screenMessage(abc, color=(1,0,0),transient=True)


#bsInternal._chatMessage('Thanks for Improving our Server')
                

