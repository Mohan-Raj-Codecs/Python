from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
import subprocess as sub

###Global VARS

###

##Startup
sub.Popen(["chrome.bat"])
options=Options()
options.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
actions = ActionChains(driver)
driver.get("https://meet.google.com/ion-afbo-uwo")
####


def Join():
    try:
        Join_Btn = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Join now')]")))
    except:
        Join_Btn = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Ask to join')]")))
    print("Located Join")
    return Join_Btn

def Precaution():
    try :
        Mic = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Turn off microphone (CTRL + D)']")))
        print("Located Mic")
        Mic.click()
        Vid = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Turn off camera (CTRL + E)']")))
        print("Located Video")
        Vid.click()

    except:
        print("Retrying to take Precaution Measures :)")
        Precaution()

def Get_Mic():
    try:
        Mic_Btn = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Turn on microphone (CTRL + D)']")))
        print("Mic is Off")
        return False
    except:
        Mic_Btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Turn off microphone (CTRL + D)']")))
        print("Mic is On")
        return True

def Set_Mic(x):
    x = True if x=="on" else (False if x=="off" else x)
    x=bool(x)

    if x!=Get_Mic():
        if x:
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Turn on microphone (CTRL + D)']"))).click()
            except:
                print("Something Strange Happend in Set Mic(On)")
        else:
            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Turn off microphone (CTRL + D)']"))).click()
            except:
                print("Something Strange Happend in Set Mic(Off)")
##Chats
def Chat_close(force=False):
    try:
        close = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']")))
        print("Found Close Btn")
        close.click()
    except:
        if force:
            Chat_close(True)
        else:
            return

def Chat_open(force=False):
    try:
        chat_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Chat with everyone']")))
        print("Found Chat box")
        chat_box.click()
    except:
        if force:
            Chat_open(force)
        else:
            return
        
def Chat_box(force=False):
    try:
        Chat_open(force)
        sleep(1)
        Chat_close()
    except:
        if force:
            print("Researching Chat Box........")
            Chat_box(force)
        else:
            return

def Chat_fetch(bot=None,force=False):
    chats=[]
    try:
        chat = driver.find_elements_by_xpath("//div[@data-message-text]")
        for i in chat:
            chats.append(i.get_attribute("data-message-text"))
    except:
        if force:
            Chat_fetch(bot,force)
        else:
            pass
    if bot==None:
        return chats
    else:
        return bot.mod(chats)

def Chat_detail(force=False):
    names=[]
    timestamps=[]
    try:
        name = driver.find_elements_by_xpath("//div[@data-sender-name]")
        timestamp = driver.find_elements_by_xpath("//div[@data-timestamp]")
    except:
        if force:
            Chat_detail(force)
        else:
            return details
    for i in name:
        names.append(i.get_attribute("data-sender-name"))
    for i in timestamp:
        timestamps.append(i.get_attribute("data-timestamp"))
    return names,timestamps

def Chat_send(x,bot=None,force=False):
    try:
        sleep(0.3)
        Chat_close()
        sleep(0.3)
        Chat_open(True)
        sleep(0.5)
        sender = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//textarea")))
        #sender.click()
        sender.send_keys(str(x))
        sleep(0.05)
        sender.send_keys(Keys.RETURN)
        Chat_close()
        print("Sent Response : ",x)
        if bot==None:
            print("Custom Chat ignore")
        else:
            bot.add(len(Chat_fetch(None,True))-1)
    except:
        if force:
            Chat_send(x,bot,force)
        else:
            return
    
####

def wait_until(func, timeout, period=0.25):
    mustend = time.time() + timeout
    while time.time() < mustend:
        try:
            if func(): return True
        except:
            continue
        time.sleep(period)
        print("Waiting : ",timeout - (mustend - time.time()) )
    return False

class evade:
    def __init__(self):
        self.vars=[]

    def add(self,x,first=False):
        if first:
            just=[0]
            just.extend(self.vars)
            just[0]=x
            self.vars=just
        else:
            self.vars.append(x)
        print("Added : ",x)

    def rem(self,x,_all=False):
        if _all:
            self.vars=list(i for i in self.vars if i!=x)
        else:
            self.vars.remove(x)

    def mod(self,x):
        x=list(x)
        for i in self.vars: #Assign Dummy
            try:
                x[i]="dummy"
            except IndexError:
                pass
##                if i==len(x):
##                    x.append(0)
##                x[i]="dummy"
        x=list(i for i in x if i!="dummy") #Remove Dummy
        return x

    def unread():
        pass

    def ret(self):
        return self.vars

def process_chat(bot,x):
    #if x in "/": #Do Something Filter
    Chat_send(str(x),bot,True)
    


Precaution()
wait_until(func=Join().click,timeout=7)
Chat_box(force=True)

old_len=0
bot_cmd = evade()
Chat_send("Hey This is Groovy , a Music Bot\nvisit : www.groovy.com to know commands",None,True)
chets=Chat_fetch(None,True)
bot_cmd.add(len(chets)-1)
bot_cmd.add(len(chets)-2)


while True:
    chats=Chat_fetch(bot_cmd,True)
    print(chats)
    print(Chat_fetch(None,True))
    if len(chats)>old_len: #Changes detected
        if len(chats)==old_len+1: #Only one chat came
            process_chat(bot_cmd,chats[len(chats)-1])
        else: #many chats came
            for i in range(old_len,len(chats)):
                process_chat(bot_cmd,chats[i])
                
    old_len=len(chats)
    sleep(0.5)


#/div data-message-text
#/div data-sender-id
#/div data-sender-name
#/div data-timestamp
#/div data-formatted-timestamp



#C:\Users\raj28\AppData\Local\Google\Chrome\User Data\Profile 5
#"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8989 --user-data-dir="C:\Users\raj28\Desktop\Py Local projects\Meet bot\Meet musiz\data"
    #aria-label="Turn off microphone (CTRL + D)"
#aria-label="Turn off camera (CTRL + E)"
