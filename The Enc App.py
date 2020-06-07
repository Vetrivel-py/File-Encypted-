import tkinter as tk
import time
from tkinter import filedialog
import pymysql as py
from tkinter import messagebox

#------Creating a Window--------
window = tk.Tk()
window.geometry("500x350")
window.title("Encryption App")
window.configure(bg="#390000")

#------Frames--------
login_frame = tk.Frame(window,height=500,width=500,bg="#390000")
login_frame.grid(column=0,row=0,sticky="news")

home_frame = tk.Frame(window, height=500,width=500,bg="#390000")
home_frame.grid(column=0,row=0,sticky ="news")

enc_frame = tk.Frame(window,height=500,width=500,bg="#390000")
enc_frame.grid(column=0,row=0,sticky="news")

denc_frame = tk.Frame(window,height='500',width='500',bg="#390000")
denc_frame.grid(column=0,row=0,sticky="news")


def Renc():
    enc_frame.tkraise()

def Rhome():
    home_frame.tkraise()

def Rdenc():
    denc_frame.tkraise()

def Rlogin():
    login_frame.tkraise()

Rlogin()

#------Functions--------

def login():
    userId = userid_entry.get()
    passWord = password_enrty.get()
    database = py.connect('localhost','root','70809900dac','auth')
    cursor = database.cursor()
    cursor.execute('Select userid from acc;')
    userid_list = []
    data = cursor.fetchall()
    for i in data:
        userid_list.append(i[0])
    for i in userid_list:
        if i==userId:
            break
        else:
            pass
    else:
        tk.messagebox.showerror("Error","Authentication failed")
        return(None)
    database.close()
    Rhome()
    return(None)

def back():
    for i in (userid_entry,password_enrty):
        i.delete(0,len(i.get()))
        i.insert(0,"")
    Rlogin()

def back_1():
    Rhome()


def encbutton():
    Renc()

def dencbutton():
    Rdenc()

def encodef(flocal):
    try:
         org=open(flocal,'r')
    except Exception:
        print("Error")
        return(None)
    data = org.read()
    ct = time.localtime()
    c = ct.tm_min
    end_data = ""

    for i in data:
        m = ord(i)
        e = m*(c**2)
        enc = str(e)+" "         
        end_data = end_data + enc

    end_data = end_data + " {0}".format(c)
    org.close()

    org = open(flocal,'w')
    org.write(end_data)
    org.close()
    return(None)

def decodef(flocal):
    try:
        org=open(flocal,'r')
    except Exception:
        print("Error")
        return(None)
    data=org.read()
    org.close()
    nums = data.split()
    c = int(nums[-1])
    end_data = ""

    for i in range(0,len(nums)-1):
        m = int(nums[i])/(c**2)
        dec=chr(int(m))
        end_data += dec

    org = open(flocal,'w')
    org.write(end_data)

    return(None)


def browsefil():
    window.filename = filedialog.askopenfilename(initialdir='/',title="Select a file",filetypes=(('text','*.txt'),)) 
    file_local = window.filename 
    encodef(file_local)
    tk.messagebox.showinfo("Info","Your file is encrypted.")
    return(None) 

def browsefill():
    window.filename = filedialog.askopenfilename(initialdir='/',title="Select a file",filetypes=(('text','*.txt'),)) 
    file_local = window.filename 
    decodef(file_local)
    tk.messagebox.showinfo("Info","Your file is decrypted")
    return(None) 

Title_label = tk.Label(login_frame,text="Encrypt/Decypt",font=("Bitter","30"),bg="#390000",fg="#fb7013")
Title_label.place(x=0,y=0) 

Email_Label = tk.Label(login_frame,text="Enter your UserID:",bg="#390000",fg="White",font=("Bitter","17"))
Email_Label.place(x=0,y=80)

Pass_Label = tk.Label(login_frame,text="Enter your Password:",bg="#390000",fg="White",font=("Bitter","17"))
Pass_Label.place(x=0,y=180)
  

userid_entry = tk.Entry(login_frame,font=("Calendula","15"),bd=6,bg="#610000",fg="White")
userid_entry.place(x=250,y=80)

password_enrty = tk.Entry(login_frame,show="\u2022",font=("Calendula","15"),bd=6,bg="#610000",fg="White")
password_enrty.place(x=250,y=175)

Enc_Button = tk.Button(home_frame, text="Encrypt",bg="#610000",fg="white", font=("Bitter","25"),border='5',activebackground="#390000",activeforeground="white",command=encbutton)
Enc_Button.place(x=80,y=80)

Denc_Button = tk.Button(home_frame,text="Decrypt",bg="#610000",fg="white",font=("Bitter","25"),border='5',activebackground="#390000",activeforeground="white",command=dencbutton)
Denc_Button.place(x=260,y=80)

browse_Button = tk.Button(enc_frame,text="Browse",bg="#610000",fg="white",font=("Bitter","25"),border='5',activebackground="#390000",activeforeground="white",command=browsefil)
browse_Button.place(x=80,y=80)

browse_Button2 = tk.Button(denc_frame,text="Browse",bg="#610000",fg="white",font=("Bitter","25"),border='5',activebackground="#390000",activeforeground="white",command=browsefill)
browse_Button2.place(x=80,y=80)

Login_button = tk.Button(login_frame,text="Login",bg="#610000",fg="White",bd=5,font=("Bitter","15"),activebackground="#390000",activeforeground="white",command=login)
Login_button.place(x=300,y=250)

Back_button = tk.Button(home_frame,text="Back",bg="#610000",fg="White",bd=5,font=("Bitter","15"),activebackground="#390000",activeforeground="white",command=back)
Back_button.place(x=340,y=250)

Back_button = tk.Button(enc_frame,text="Back",bg="#610000",fg="White",bd=5,font=("Bitter","15"),activebackground="#390000",activeforeground="white",command=back_1)
Back_button.place(x=340,y=250)

Back_button = tk.Button(denc_frame,text="Back",bg="#610000",fg="White",bd=5,font=("Bitter","15"),activebackground="#390000",activeforeground="white",command=back_1)
Back_button.place(x=340,y=250)

window.mainloop()
