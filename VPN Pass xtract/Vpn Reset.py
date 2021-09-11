from bs4 import BeautifulSoup as bs
import requests as req
import time
import dload
from PIL import Image
import os
import subprocess

new_stat=0

def cd(x):                      #cmd Process handler
    subprocess.call(str(x),shell=True)
def conect(web):                        #Check Connectivity
    try:
        source=req.get(web).text
    except : #No Internet Handling
        print("Please Connect to internet : ( \n\n")
        print("Retrying in 5")
        time.sleep(1)
        print("Retrying in 4")
        time.sleep(1)
        print("Retrying in 3")
        time.sleep(1)
        print("Retrying in 2")
        time.sleep(1)
        print("Retrying in 1")
        time.sleep(1)
        print("Retrying .........................\n\n")
        conect(web)
    try:
        soup=bs(source,'lxml')
    except UnboundLocalError :   #Assignment Error Handling
        source=req.get(web).text
        soup=bs(source,'lxml')
    return soup

def save(url,file):              #Saves a Downloaded File Over Internet
    dload.save(str(url),str(file))
    print("Saved File : ",str(file))

def dire(File):                    #Listing Directory
    Files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if File in Files:
        return True
    else:
        return False
def status(stat,err=0):     #Process Register
    global new_stat
    if err!=0 :
        print("An Error Occured After the : ",new_stat)
    else:
        new_stat=stat
        print(stat)

def vpn():
    status("Connecting ...............")
    vpn="https://vpnbook.com"
    soup=conect(vpn)
    try :
        status("Grabbing ..........")
        uls=soup.find_all("ul",{"class":"square"})   #Tracking Absolute Place
        for ul in uls:
            for li in ul.find_all("li"):            
                for strong in li.find_all("strong"):
                    for img in strong.find_all("img"):
                        if (str(img['src']).find("password"))  >= 0:
                            paswd=vpn+"/"+img['src']+".png"
        print(paswd)
        status("Saving.................")
        save(paswd,"pass.png")
        def saver():
            if dire("pass.png"):
                status("Resizing Image For Better Recognizing it.............")
                im=Image.open("pass.png")
                resized=im.resize((round(im.size[0]*2),round(im.size[1]*2)))
                resized.save("password.png")
                cd("del pass.png")
            else :
                print("File not Found :( ")
                status("Retrying to Catch the File ......")
                save(paswd,"pass.png")
                saver()
        saver()

        status("Scanning Image with OCR..........")
        cd("copy password.png OCR /Y")
        cd("cd OCR && tesseract.exe password.png out")
        cd("cd OCR && copy out.txt ..")

        with open("out.txt","r") as f:
            paswd=f.read().strip()
            
        cd("del out.txt")
        print(paswd)
        status("Creating VPN Powershell Script..............")
        with open('vpn.ps1','w') as f:
            f.write('''get-vpnconnection | Remove-VpnConnection -Force
Add-VpnConnection -Name "us server" -ServerAddress "us1.vpnbook.com" -TunnelType "Pptp" -AuthenticationMethod MSChapv2 -RememberCredential -PassThru -Force
Install-Module -Name VPNCredentialsHelper -Force
Get-ExecutionPolicy -List
Set-ExecutionPolicy Unrestricted -Force
Set-VpnConnectionUsernamePassword -connectionname "us server" -username "vpnbook" -password '''+paswd+'''
rasdial "us server" vpnbook '''+paswd+'''

''')
        status("Executing VPN Scipt as Admin................")
        cd('''PowerShell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process PowerShell -ArgumentList '-ExecutionPolicy Unrestricted','-File \\"'''+os.path.join(os.getcwd()+'\\vpn.ps1')+'''\\"' -Verb RunAs"''')
        time.sleep(2)
        status("Cleaning up Chunk Data...............")
        cd("del password.png")
        cd("cd OCR && del password.png")
        cd("cd OCR && del out.txt")
        cd("del vpn.ps1")
        
    except :
        cd("del password.png")
        cd("cd OCR && del password.png")
        cd("cd OCR && del out.txt")
        cd("del vpn.ps1")
        cd('cls && color 04')
        print("\n\n\n\n\n\n")
        status(stat="101",err=1)
        cd('pause')

    finally:
        pass

vpn()
