import cv2
import numpy as np
from time import perf_counter
import datetime
from tkinter import *
from SMS import send_alert
import threading
from PIL import ImageTk, Image
import time
import tkinter as tk
import os

screen = tk.Tk()
screen.title("SPOT")
screen.geometry("1000x700")
screen.config(bg="white")
screen.resizable(False, False)

bc = "white"
fc = "#0000A3"

# Nippy Embed
cascade= cv2.CascadeClassifier("./input/training_data/russian.xml")
part_seconds=30
resetter = perf_counter()
last_move = perf_counter()
last_sms = perf_counter()
last_sent = 0
person = 0


def clock():
    clock_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=clock_time)
    clock_label.after(1000, clock)


def login():
    global add_button
    global view_button
    
    u = username_e.get()
    p = password_e.get()
    
    if len(u) and len(p)!=0:
        # open specific user profile
        r = open("CaotUsers.txt", "r")
        re = r.readlines()
        authorized=False
        for i in re:
            if u in i.split(" ")[0] and p in i.split(" ")[1] :
                authorized=True
                
        if authorized :
            username_l.destroy()
            username_e.destroy()

            password_l.destroy()
            password_e.destroy()

            login_button.destroy()
            signup_button.destroy()

            live_button = Button(screen, text="Live", fg=fc, bg="black", font=("arial", 17), command=lambda: watch("cam"), height=2, width=7)
            live_button.place(x=70, y=100)

            show_button = Button(screen, text="Show", fg=fc, bg="black", font=("arial", 17), command=lambda: watch("vid"), height=2, width=7)
            show_button.place(x=70, y=200)

            exit_button = Button(screen, text="Exit", fg=fc, bg="black", font=("arial", 17), command=lambda: os._exit(0), height=2, width=7)
            exit_button.place(x=70, y=400)

        else:
            cpl = Label(screen, text="Profile not found!", font=("arial black", 20, 'bold'), fg=fc, bg=bc)
            cpl.place(x=430, y=430)
    else:
        cpl = Label(screen, text="Please enter user credentials!", font=("arial black", 20, 'bold'), fg=fc, bg=bc)
        cpl.place(x=310, y=430)


def signin():
    global cpassword_e
    global cpassword_l
    global signin_button

    u = username_e.get()
    p = password_e.get()
    cp = cpassword_e.get()

    if len(p) >= 7:
        if p == cp:
            file = open("CaotUsers.txt", "a")
            userpass = u+" "+p
            file.write(userpass+"\n")
            file.close()

        else:
            global ppl
            ppl = Label(screen, text="Passwords don't match", font=("arial black", 10, 'bold'), fg=fc, bg=bc)
            ppl.place(x=430, y=430)
            return
    else:
        global cpl
        cpl = Label(screen, text="Password must be minimum of 7 characters", font=("arial black", 10, 'bold'), fg=fc, bg=bc)
        cpl.place(x=400, y=430)
        return
    try:
        ppl.destroy()
        cpl.destroy()
    except:
        pass
    username_e.delete(0, END)
    password_e.delete(0, END)
    cpassword_e.delete(0, END)
    
    username_l.destroy()
    username_e.destroy()

    password_l.destroy()
    password_e.destroy()

    login_button.destroy()
    signup_button.destroy()

    cpassword_e.destroy()
    cpassword_l.destroy()

    signin_button.destroy()

    live_button = Button(screen, text="Live", fg=fc, bg="black", font=("arial", 17), command=lambda: watch("cam"), height=2, width=7)
    live_button.place(x=70, y=100)

    show_button = Button(screen, text="Show", fg=fc, bg="black", font=("arial", 17), command=lambda: watch("vid"), height=2, width=7)
    show_button.place(x=70, y=200)

    exit_button = Button(screen, text="Exit", fg=fc, bg="black", font=("arial", 17), command=exit, height=2, width=7)
    exit_button.place(x=70, y=400)


def signup():
    global cpassword_e
    global signin_button
    global cpassword_l

    login_button.destroy()
    signup_button.destroy()

    # confirm password
    cpassword_l = Label(screen, text="Confirm Password", font=("arial black", 16, 'bold'), fg="blue", bg="black")
    cpassword_l.place(x=410, y=360)

    cpassword_e = Entry(screen, show="*", font=("arial black", 13, 'bold'), width=30, fg=fc, bg=bc)
    cpassword_e.place(x=340, y=400)

    signin_button = Button(screen, text="Sign in", width=7, height=2, fg="blue", bg="black", command=signin)
    signin_button.place(x=470, y=500)


def get_time():
    x = datetime.datetime.now()
    return x.strftime("%d")+x.strftime("%b")+x.strftime("%Y")+x.strftime("%H")+x.strftime("%M")+x.strftime("%S")+".avi"


def watch(mode, files="output.avi"):
    global last_move, last_sms, last_sent, person, resetter,out
    cap = cv2.VideoCapture(0) if(mode == "cam") else cv2.VideoCapture("./input/in.avi")
    #cap = cv2.VideoCapture(0) if(mode == "cam") else cv2.VideoCapture("./input/final_12.avi")
        
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    out = cv2.VideoWriter("./output/"+get_time(), fourcc, 10, (1280, 720))

    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def person_detect(frame):
        global person
        bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.02)
        person = 1
        for x, y, w, h in bounding_box_cordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1

        if (person > 1):
            last_move = perf_counter()
            return True
        else:
            return False
        # return frame

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    print(frame1.shape)
    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Car LPR Detection
        nplate=cascade.detectMultiScale(gray,1.1,4)
        for (x,y,w,h) in nplate:
            wT,hT,cT=frame1.shape
            a,b=(int(0.02*wT),int(0.02*hT))
            plate=frame1[y+a:y+h-a,x+b:x+w-b,:]
            #make the img more darker to identify LPR
            kernel=np.ones((1,1),np.uint8)
            plate=cv2.dilate(plate,kernel,iterations=1)
            plate=cv2.erode(plate,kernel,iterations=1)
            plate_gray=cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,255,0),2)
            print("Detected LP :))))))))))))))))))))))))))))))))))))))))))")
            cv2.imwrite("./output/number_plate/"+get_time()+"Result.png",plate)
            
        # Detection
        if (len(contours) > 7):
            # Human Detection
            if (person_detect(frame1) or (perf_counter() - last_move) < 2):  # Record for a while
                # Noting Human Detection
                print(perf_counter()-last_sms)
                print(last_sent,person-1,last_move)
                if((perf_counter()-last_sms)>10 and (last_sent<=person-1)):
                    #Sending Data
                    t1=threading.Thread(target=send_alert,args=(person-1,))
                    t1.start()
                    last_sms = perf_counter()
                    last_sent = person-1
                image = cv2.resize(frame2, (1280, 720))
                #Part File Logic
                if((perf_counter()-resetter) > part_seconds):
                    resetter=perf_counter()
                    out.release()
                    out = cv2.VideoWriter("./output/"+get_time(), fourcc, 10, (1280, 720))
                    print("Parting File Here")
                out.write(image)
                print("Person with Moving")
            else:
                person = 0
                print("No Person Found")

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 900:
                continue
            #cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

# created a label and display video there
        l = Label(screen, bg="grey")
        l.place(x=200, y=100)
# cv2.imshow("feed", frame1)
        frame1 = ImageTk.PhotoImage(Image.fromarray(frame1))
        l['image'] = frame1
        screen.update()
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    out.release()


im = ImageTk.PhotoImage(Image.open("l5.jpg"))

spot_label = tk.Label(screen, image = im, fg=fc, bg=bc, font=("arial black", 22, "bold"))
spot_label.place(x=370, y=1)

caot_label = Label(screen, text="Powered by CAOT", fg=fc, bg=bc, font=("arial", 13, "bold"))
caot_label.place(x=830, y=670)

username_l = Label(screen, text="USER", font=("arial", 20, "bold"), fg=fc, bg=bc)
username_l.place(x=460, y=140)

username_e = Entry(screen, font=("arial", 13), width=30, fg=fc, bg=bc)
username_e.place(x=370, y=200)
u = username_e.get()
username_e.focus_set()

password_l = Label(screen, text="PASSWORD", font=("arial", 20, "bold"), fg=fc, bg=bc)
password_l.place(x=430, y=260)

password_e = Entry(screen, width=30, show="*", font=("arial", 13), fg=fc, bg=bc)
password_e.place(x=370, y=310)

login_button = Button(screen, text="Login", width=7, height=2, fg="blue", bg=bc, command=login)
login_button.place(x=470, y=370)

signup_button = Button(screen, text="Signup", width=7, height=2, fg="blue", bg=bc, command=signup)
signup_button.place(x=470, y=510)

ue_box = Text(screen, height=10, width=30, font=("arial black", 10, 'bold'), fg=fc, bg=bc)

clock_label = Label(screen, text="", font=("arial", 16, "bold"), fg=fc, bg=bc)
clock_label.place(x=10, y=670)
clock()

screen.mainloop()
