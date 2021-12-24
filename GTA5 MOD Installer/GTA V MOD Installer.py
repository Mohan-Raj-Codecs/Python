from subprocess import call
from os import getcwd
from time import sleep

def cal(x):
    x = str(x)
    call(x, shell=True)
    
def de(x):
    return str("del \""+str(x)+"\" /q /s\n")
def der(x):
    return str("RD /q /s \""+str(x)+"\" \n")

def uninstall():
    
    uninstall_code = str('@echo off\n'+der("menyooStuff")+der("scripts")+de("ScriptHookVDotNet3.xml")+de("ScriptHookVDotNet3.dll")+de("ScriptHookVDotNet2.xml")+de("ScriptHookVDotNet2.dll")+de("ScriptHookVDotNet.ini")+de("ScriptHookVDotNet.asi")+de("ScriptHookV.dll")+de("NativeTrainer.asi")+de("Menyoo.asi"))
    misc_files=str(de("exclude.txt")+de("GTA V MOD Installer.py")+de("menyooLog.log")+de("ScriptHookVDotNet.log")+de("ScriptHookV.log")+de("asiloader.log"))
    openiv_except=str('for %%i in (*.asi) do if not "%%~i" == "OpenIV.asi" del "%%~i" \n')
    self_destruct=str(de("MOD Uninstaller.bat")+"@echo on")
        
    with open('MOD Uninstaller.bat', 'w') as f:
        f.write(uninstall_code+misc_files+openiv_except+self_destruct)
    f.close()

    with open('exclude.txt', 'w') as f:
        f.write(".py\n.txt\n")
    f.close()


uninstall()
GTAV = input('Enter the path of GTAV : ')
GTA = GTAV
GTAV = '"' + GTAV + '"'
Sou = str(getcwd())
So = Sou
Sou = '"' + Sou + '"'
cal('xcopy /E /I /Y /EXCLUDE:exclude.txt  * ' + GTAV)
cal('color A0')
print('                           MOD Installed :)')
cal(de('MOD Uninstaller.bat'))
cal(de('exclude.txt'))
sleep(5)
