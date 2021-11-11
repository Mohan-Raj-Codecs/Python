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
driver.get("https://meet.google.com/vqm-ynno-wnf")
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
        Chat_close(force)
    except:
        if force:
            print("Researching Chat Box........")
            Chat_box(force)
        else:
            return

def Chat_fetch(force=False):
    chats=[]
    try:
        chat = driver.find_elements_by_xpath("//div[@data-message-text]")
    except:
        if force:
            Chat_fetch(force)
        else:
            return chats
    for i in chat:
        chats.append(i.get_attribute("data-message-text"))
    return chats

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

def Chat_send(x):
    pass
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




Precaution()
wait_until(func=Join().click,timeout=7)
Chat_box(force=True)

    
while True:
    chats=Chat_fetch(True)
    names,times=Chat_detail(True)
    print(len(chats))
    for i in range(len(chats)):
        try:
            print(names[i]," : ",chats[i]," : ",times[i])
        except IndexError:
            for j in range(i-1,100):
                try:
                    print(names[i-j]," : ",chats[i]," : ",times[i-j])
                    break
                except IndexError:
                    pass
                
    sleep(1)



#/div data-message-text
#/div data-sender-id
#/div data-sender-name
#/div data-timestamp
#/div data-formatted-timestamp



#C:\Users\raj28\AppData\Local\Google\Chrome\User Data\Profile 5
#"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8989 --user-data-dir="C:\Users\raj28\Desktop\Py Local projects\Meet bot\Meet musiz\data"
    #aria-label="Turn off microphone (CTRL + D)"
#aria-label="Turn off camera (CTRL + E)"
