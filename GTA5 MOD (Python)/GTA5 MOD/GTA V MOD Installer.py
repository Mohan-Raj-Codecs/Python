from subprocess import call
from os import getcwd

def c(x):
    x = str(x)
    call(x, shell=True)


def u():
    abc = '@echo off\ndel Menyoo.asi /q /s\nRD /q /s menyooStuff\ndel ScriptHookV.dll /q /s\ndel NativeTrainer.asi /q /s\ndel dinput8.dll /q /s\ndel "MOD Uninstaller.bat"'
    with open('MOD Uninstaller.bat', 'w') as (f):
        f.write(abc)
    f.close()


u()
GTAV = input('Enter the path of GTAV : ')
GTA = GTAV
GTAV = '"' + GTAV + '"'
Sou = str(getcwd())
So = Sou
Sou = '"' + Sou + '"'
c('xcopy /E /I *.* ' + GTAV)
c('del "' + GTA + '\\MOD Installer.exe"')
c('color A0')
print('MOD Installed :)')
