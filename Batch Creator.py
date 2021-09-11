admin='''
@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------
'''
a=[]
txt=''


def Creator(txt='',f_name='batch'):
    f_name+='.bat'
    with open(f_name,'w') as f:
        f.write(str(txt))
    f.close()

filename=input("Enter the File name to create (without extension) : ")
b=input("Do you want Admin Priviledge in your bat File (yes/no): ")
if b=='yes' or 'Yes' or 'y' :
    txt=admin
    print("Your Commands will be Run as Administrator!!!!! :) ")

while True:
    i=input("Enter the command : ")
    if i=="":
        break
    a.append(str(i))

for i in a:
    txt+=i+'\n'

txt+='\npause'

try:
    Creator(txt,filename)
    print("Batch File Created SuccessFully :)")
except:
    print("Cannot Create bat File Right Now :( ")
    
