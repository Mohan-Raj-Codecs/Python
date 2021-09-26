from tkinter import *
from time import *
from subprocess import *
from random import randint
call('color 0A', shell=True)
call('title Loading', shell=True)

def up(x):
    x = int(x)
    for o in range(0, x):
        print('\n')


def cl():
    call('cls', shell=True)
    print('Loading.....')


def Rock(x):
    roc = '                                ^\n                               |2|\n                               |1|\n                              /Roc\\\n                             /!@$%@\\\n                            |-------|\n                            |%% M %%|\n                            |!! O !!|\n                            |`` H ``|\n                            |[] A ]]|\n                            |{} N {}|\n                            |() R )(|\n                            |&& A&&&|\n                            |@@ J@@@|\n                           /$$$$$$$$\\\n                          /##########\\\n                         /~~~~~~~~~~~~\\\n                        /<><><><><><><>\\\n                       /||||||||||||||||\\\n                      /__________________\\ '
    if x < 14:
        roc = '                                ^\n                               |2|\n                               |1|\n                              /Roc\\\n                             /!@$%@\\\n                            |-------|\n                            |%% M %%|\n                            |!! O !!|\n                            |`` H ``|\n                            |[] A ]]|\n                            |{} N {}|\n                            |() R )(|\n                            |&& A &&|\n                            |@@ J @@|\n                           /$$$$$$$$\\\n                          /##########\\\n                         /~~~~~~~~~~~~\\\n                        /<><><><><><><>\\\n                       /||||||||||||||||\\\n                      /__________________\\\n                         |||||||||||||||\n                          |||||||||||||\n                            |||||||||\n                             |||||||\n                               |||\n                                |'
    print(roc)


def ex(z):
    z = int(z)
    zo = ' '
    if z == 19:
        zo = '                         |||||||||||||||'
    if z == 18:
        zo = '                         |||||||||||||||\n                          |||||||||||||'
    if z == 17:
        zo = '                         |||||||||||||||\n                          |||||||||||||\n                            |||||||||'
    if z == 16:
        zo = '                         |||||||||||||||\n                          |||||||||||||\n                            |||||||||\n                              ||||||'
    if z == 15:
        zo = '                         |||||||||||||||\n                          |||||||||||||\n                            |||||||||\n                             |||||||\n                               |||'
    if z == 14:
        zo = '                         |||||||||||||||\n                          |||||||||||||\n                            |||||||||\n                             |||||||\n                               |||\n                                |'
    else:
        print(zo)


def exe(s):
    cl()
    up(s)
    Rock(s)
    ex(s)


print('                         ^')
sleep(0.1)
print('                        |2|')
sleep(0.1)
print('                        |1|')
sleep(0.1)
print('                       /Roc\\')
sleep(0.1)
print('                      /!@$%@\\')
sleep(0.1)
print('                     |-------|')
sleep(0.1)
print('                     |%% M %%|')
sleep(0.1)
print('                     |!! O !!|')
sleep(0.1)
print('                     |`` H ``|')
sleep(0.1)
print('                     |[] A ]]|')
sleep(0.1)
print('                     |{} N {}|')
sleep(0.1)
print('                     |() R )(|')
sleep(0.1)
print('                     |&& A &&|')
sleep(0.1)
print('                     |@@ J @@|')
sleep(0.1)
print('                    /$$$$$$$$\\')
sleep(0.1)
print('                   /##########\\')
sleep(0.1)
print('                  /~~~~~~~~~~~~\\')
sleep(0.1)
print('                 /<><><><><><><>\\')
sleep(0.1)
print('                /||||||||||||||||\\')
sleep(0.1)
print('               /__________________\\ ')
sleep(1)
for za in range(20, 0, -1):
    sleep(0.1)
    exe(za)

cl()
a = 'Password '
path = 'En(or)Decrypt.txt'

def Wr(a, x):
    a = a + ' : '
    with open(path, 'a') as (f):
        f.write(a)
        f.write(x)
        f.write('                   Written on  : ' + asctime())
        f.write('\n')


def bo():
    s = en5.get()
    o = len(s)
    w = ''
    for i in range(o):
        if i % 2 == 0:
            w = w + s[i]

    Wr('Modified ' + a, w)
    en6.delete(0, END)
    en6.insert(0, w)


def de():
    if en1.get() == '12':
        if en3.get() == '12':
            ss()
    word = ''
    s = en3.get()
    for x in s:
        y = ord(x)
        y = int(y)
        y = y - 1
        z = chr(y)
        word = word + z

    Wr('Decrypted ' + a, word)
    en4.delete(0, END)
    en4.insert(0, word)


def en():
    if en1.get() == '12':
        if en3.get() == '12':
            ss()
    word = ''
    s = en1.get()
    tea = ''
    for y in s:
        tea = tea + y + chr(randint(30, 100))

    s = tea
    for x in s:
        y = ord(x)
        y = int(y)
        y = y + 1
        z = chr(y)
        word = word + z

    Wr('Encrypted ' + a, word)
    en2.delete(0, END)
    en2.insert(0, word)


aq = input()
if aq == '12':
    pass
else:
    print('\n\n\n\n\n\n\n\n                   You cannot Pass Through our Firewall')
    print('\n\n                                  System Halted  :(')
    sleep(3)
    exit()
w = Tk()
w.title('En(or)Decrypting')
la1 = Label(w, text='*_*_*_*_*_*_*_*_*_*_*_*_*_*_', bg='blue').grid(row=0, column=1)
la2 = Label(w, text='ENCODING', width=20, height=3, bg='green', fg='red').grid(row=1, column=1)
la3 = Label(w, text='*_*_*_*_*_*_*_*_*_*_*_*_*_*_', bg='blue').grid(row=2, column=1)
la4 = Label(w, text='Enter the Words to encode : ', bg='violet').grid(row=4, column=0)
en1 = Entry(w, bg='yellow', fg='black', borderwidth=5, width=35)
en1.grid(row=4, column=1)
bt1 = Button(w, text='Encode This!', width=10, height=3, bg='red', command=en)
bt1.grid(row=2, column=2, rowspan=5)
la5 = Label(w, text='Encoded the words : ', fg='green').grid(row=5, column=0)
en2 = Entry(w, bg='yellow', fg='black', borderwidth=5, width=35)
en2.grid(row=5, column=1)
la12 = Label(w, text='').grid(row=6, column=0)
la13 = Label(w, text='').grid(row=14, column=0)
la14 = Label(w, text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', fg='white', bg='black').grid(row=7, column=0, columnspan=3)
la15 = Label(w, text='').grid(row=8, column=0)
la6 = Label(w, text='*_*_*_*_*_*_*_*_*_*_*_*_*_*_', bg='violet').grid(row=9, column=1)
la7 = Label(w, text='DECODING', width=20, height=3, bg='red', fg='yellow').grid(row=10, column=1)
la8 = Label(w, text='*_*_*_*_*_*_*_*_*_*_*_*_*_*_', bg='violet').grid(row=11, column=1)
la9 = Label(w, text='Enter the Words to decode : ', bg='pink').grid(row=12, column=0)
en3 = Entry(w, bg='yellow', fg='black', borderwidth=5, width=35)
en3.grid(row=12, column=1)
bt2 = Button(w, text='Decode This!', width=10, height=3, bg='blue', command=de)
bt2.grid(row=12, column=2, rowspan=2)
la10 = Label(w, text='Decoded the words : ', fg='red').grid(row=13, column=0)
en4 = Entry(w, bg='yellow', fg='black', borderwidth=5, width=35)
en4.grid(row=13, column=1)
la16 = Label(w, text='').grid(row=15, column=0)
la17 = Label(w, text='').grid(row=16, column=0)
la18 = Label(w, text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', fg='white', bg='black').grid(row=17, column=0, columnspan=3)
la19 = Label(w, text='').grid(row=18, column=0)

def ss():
    global bt3
    global en5
    global en6
    la20 = Label(w, text='*_*_*_*_*_*_*_*_*_*_*_*_*_*_', bg='orange').grid(row=19, column=1)
    la21 = Label(w, text='BONUS', width=20, height=3, bg='red', fg='blue').grid(row=20, column=1)
    la22 = Label(w, text='*_*_*_*_*_*_*_*_*_*_*_*_*_*_', bg='orange').grid(row=21, column=1)
    la23 = Label(w, text='Enter the Words to extra  decode : ', fg='white', bg='black').grid(row=22, column=0)
    en5 = Entry(w, bg='yellow', fg='black', borderwidth=5, width=35)
    en5.grid(row=22, column=1)
    bt3 = Button(w, text='Decode This!', width=10, height=3, bg='green', command=bo)
    bt3.grid(row=22, column=2, rowspan=2)
    la24 = Label(w, text='Decoded the words : ', fg='red').grid(row=23, column=0)
    en6 = Entry(w, bg='yellow', fg='black', borderwidth=5, width=35)
    en6.grid(row=23, column=1)
    la25 = Label(w, text='').grid(row=24, column=0)


la26 = Label(w, text=' Dont Worry The Passwords are Logged You can access it in your directory', fg='red').grid(row=25, column=0, columnspan=3)
w.mainloop()
