import time
import subprocess as sub
import os
theme='''

[Dark Theme]
normal-foreground = #ffffff
normal-background = #1a1a1a
keyword-foreground = #ff7700
keyword-background = #1a1a1a
builtin-foreground = #ff1aff
builtin-background = #1a1a1a
comment-foreground = #dd0000
comment-background = #1a1a1a
string-foreground = #00aa00
string-background = #1a1a1a
definition-foreground = #0080ff
definition-background = #1a1a1a
hilite-foreground = #000000
hilite-background = gray
break-foreground = black
break-background = #ffff55
hit-foreground = #ffffff
hit-background = #009d27
error-foreground = #000000
error-background = #ff2828
context-foreground = #c0c0c0
context-background = #1a1a1a
linenumber-foreground = gray
linenumber-background = #ffffff
cursor-foreground = #ffffff
stdout-foreground = #00d5d5
stdout-background = #1a1a1a
stderr-foreground = #ff4040
stderr-background = #1a1a1a
console-foreground = #c0c0c0
console-background = #1a1a1a

'''
highlight='''
# IDLE reads several config files to determine user preferences.  This
# file is the default config file for idle highlight theme settings.

[IDLE Classic]
normal-foreground= #000000
normal-background= #ffffff
keyword-foreground= #ff7700
keyword-background= #ffffff
builtin-foreground= #900090
builtin-background= #ffffff
comment-foreground= #dd0000
comment-background= #ffffff
string-foreground= #00aa00
string-background= #ffffff
definition-foreground= #0000ff
definition-background= #ffffff
hilite-foreground= #000000
hilite-background= gray
break-foreground= black
break-background= #ffff55
hit-foreground= #ffffff
hit-background= #000000
error-foreground= #000000
error-background= #ff7777
context-foreground= #000000
context-background= lightgray
linenumber-foreground= gray
linenumber-background= #ffffff
#cursor (only foreground can be set, restart IDLE)
cursor-foreground= black
#shell window
stdout-foreground= blue
stdout-background= #ffffff
stderr-foreground= red
stderr-background= #ffffff
console-foreground= #770000
console-background= #ffffff

[IDLE New]
normal-foreground= #000000
normal-background= #ffffff
keyword-foreground= #ff7700
keyword-background= #ffffff
builtin-foreground= #900090
builtin-background= #ffffff
comment-foreground= #dd0000
comment-background= #ffffff
string-foreground= #00aa00
string-background= #ffffff
definition-foreground= #0000ff
definition-background= #ffffff
hilite-foreground= #000000
hilite-background= gray
break-foreground= black
break-background= #ffff55
hit-foreground= #ffffff
hit-background= #000000
error-foreground= #000000
error-background= #ff7777
context-foreground= #000000
context-background= lightgray
linenumber-foreground= gray
linenumber-background= #ffffff
#cursor (only foreground can be set, restart IDLE)
cursor-foreground= black
#shell window
stdout-foreground= blue
stdout-background= #ffffff
stderr-foreground= red
stderr-background= #ffffff
console-foreground= #770000
console-background= #ffffff

[IDLE Dark]
comment-foreground = #dd0000
console-foreground = #ff4d4d
error-foreground = #FFFFFF
hilite-background = #7e7e7e
string-foreground = #02ff02
stderr-background = #002240
stderr-foreground = #ffb3b3
console-background = #002240
hit-background = #fbfbfb
string-background = #002240
normal-background = #002240
hilite-foreground = #FFFFFF
keyword-foreground = #ff8000
error-background = #c86464
keyword-background = #002240
builtin-background = #002240
break-background = #808000
builtin-foreground = #ff00ff
definition-foreground = #5e5eff
stdout-foreground = #c2d1fa
definition-background = #002240
normal-foreground = #FFFFFF
cursor-foreground = #ffffff
stdout-background = #002240
hit-foreground = #002240
comment-background = #002240
break-foreground = #FFFFFF
context-foreground= #ffffff
context-background= #454545
linenumber-foreground= gray
linenumber-background= #002240

'''
conmain=r'''
# IDLE reads several config files to determine user preferences.  This
# file is the default config file for general idle settings.
#
# When IDLE starts, it will look in
# the following two sets of files, in order:
#
#     default configuration files in idlelib
#     --------------------------------------
#     config-main.def         default general config file
#     config-extensions.def   default extension config file
#     config-highlight.def    default highlighting config file
#     config-keys.def         default keybinding config file
#
#     user configuration files in ~/.idlerc
#     -------------------------------------
#     config-main.cfg         user general config file
#     config-extensions.cfg   user extension config file
#     config-highlight.cfg    user highlighting config file
#     config-keys.cfg         user keybinding config file
#
# On Windows, the default location of the home directory ('~' above)
# depends on the version.  For Windows 10, it is C:\Users\<username>.
#
# Any options the user saves through the config dialog will be saved to
# the relevant user config file. Reverting any general or extension
# setting to the default causes that entry to be wiped from the user
# file and re-read from the default file.  This rule applies to each
# item, except that the three editor font items are saved as a group.
#
# User highlighting themes and keybinding sets must have (section) names
# distinct from the default names.  All items are added and saved as a
# group. They are retained unless specifically deleted within the config
# dialog. Choosing one of the default themes or keysets just applies the
# relevant settings from the default file.
#
# Additional help sources are listed in the [HelpFiles] section below
# and should be viewable by a web browser (or the Windows Help viewer in
# the case of .chm files). These sources will be listed on the Help
# menu.  The pattern, and two examples, are:
#
# <sequence_number = menu item;/path/to/help/source>
# 1 = IDLE;C:/Programs/Python36/Lib/idlelib/help.html
# 2 = Pillow;https://pillow.readthedocs.io/en/latest/
#
# You can't use a semi-colon in a menu item or path.  The path will be
# platform specific because of path separators, drive specs etc.
#
# The default files should not be edited except to add new sections to
# config-extensions.def for added extensions.  The user files should be
# modified through the Settings dialog.

[General]
editor-on-startup= 0
autosave= 0
print-command-posix=lpr %%s
print-command-win=start /min notepad /p %%s
delete-exitfunc= 1

[EditorWindow]
width= 80
height= 40
cursor-blink= 1
font= TkFixedFont
# For TkFixedFont, the actual size and boldness are obtained from tk
# and override 10 and 0.  See idlelib.config.IdleConf.GetFont
font-size= 10
font-bold= 0
encoding= none
line-numbers-default= 0

[PyShell]
auto-squeeze-min-lines= 50

[Indent]
use-spaces= 1
num-spaces= 4

[Theme]
default= 1
name= IDLE Classic
name2=
# name2 set in user config-main.cfg for themes added after 2015 Oct 1

[Keys]
default= 1
name=
name2=
# name2 set in user config-main.cfg for keys added after 2016 July 1

[History]
cyclic=1

[HelpFiles]

'''

def s(x):
    time.sleep(float(x))
def color(x):
    if str(x)=='g':
        sub.call('color 0A',shell=True)
    elif str(x)=='r':
        sub.call('color 04',shell=True)
    elif str(x)=='w':
        sub.call('color 07',shell=True)
def cd(x):
    x=str(x)
    new = str(os.getcwd())+'\\'+x+'\\'
    os.chdir(new)

def apply():
    with open('config-highlight.def','r') as hli:
        if hli.read().find('Dark Theme')==-1:   #UnExpected Error Handling (Error 1)
            hli.close()
            sub.call('copy config-highlight.def config-highlight_old.def',shell=True)
            sub.call('copy config-main.def config-main_old.def',shell=True)
            with open('config-highlight.def','a') as hli:
                hli.write(theme)
                hli.close()
            with open('config-main.def','r') as hli:
                con = hli.read()
                merge = con[con.find('[Theme]'):int(con.find('[Theme]'))+110]
                writ = int(con.find('[Theme]')+merge.find('name2=')+6)
                hli.close()
            with open('config-main.def','w') as hli:
                be = con[:writ]
                af = con[writ:]
                mid = ' Dark Theme'
                hli.    write(be+mid+af)
        color('g')
        print('\n\n                    Successfully Applied the Dark Theme')
        print('                    Relaunch the Python Idle to See Changes')
        s(5)
    
def dismiss():
    di=str(sub.check_output('dir',shell=True))
    if di.find('config-main_old.def')==-1:     #UnExpected Error Handling (Error 2)
        print("\n\n                    Cannot Find Restore Point :( ")
        color('r')
        s(6)
        color('g')
        print("                    We can Still Fix it :) Don't Worry ")
        s(4)
        color('w')
        with open('config-highlight.def','w') as f:
            f.write(highlight)
        with open('config-main.def','w') as u:
            u.write(conmain)
        f.close()
        u.close()
        color('g')
        print("                    Sucessfully Fixed Issue")
        print("                    Successfully Uninstalled Applied Theme")
        s(3)
        
    else :
        sub.call('del config-main.def',shell=True)
        sub.call('del config-highlight.def',shell=True)
        sub.call('ren config-highlight_old.def config-highlight.def',shell=True)
        sub.call('ren config-main_old.def config-main.def',shell=True)
        color('g')
        print("\n\n                    Sucessfully Uninstalled the Applied Theme")
        s(2)
    

print("Current Directory: ",os.getcwd())
cd('Lib')
cd('idlelib')

print("         1 .Apply Dark Theme")
print("         2 .Remove Dark Theme")
a=int(input("\n\nEnter the Option you want (1/2) : "))
if a==1:
    apply()
elif a==2:
    dismiss()
else:
    print('invalid input :(  ')
    color('r')
    s(3)
sub.call('exit',shell=True)





