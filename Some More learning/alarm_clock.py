from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
import winsound

wn=Tk()
wn.title("Alarm Clock")
hour_var=StringVar()
label1=ttk.Label(wn,text="Set Alarm Hours: ",font="arial",foreground="red")
label1.grid(row=0,column=0)

hor=list(range(1,25))
hour=ttk.Combobox(wn,values=hor,textvariable=hour_var,state="readonly")
hour.grid(row=0,column=1)

mon=list(range(1,61))
min_var=StringVar()
label2=ttk.Label(wn,text="Set Alarm Minutes: ",font="arial",foreground="red")
label2.grid(row=1,column=0)
minutes=ttk.Combobox(wn,values=mon,textvariable=min_var,state="readonly")
minutes.grid(row=1,column=1)
# minutes.grid(row=0,)

r = 600  # hz, change this as needed
g = 2 ** (1.0 / 12.0)
Sa = r
Re_k = r * g
Re = r * g ** 2
Ga_k = r * g ** 3
Ga = r * g ** 4
Ma = r * g ** 5
Ma_t = r * g ** 6
Pa = r * g ** 7
Dha_k = r * g ** 8
Dha = r * g ** 9
Ni_k = r * g ** 10
Ni = r * g ** 11

song_list=[Dha_k,Ni_k,Ni,Ni_k,Ma_t,Ni_k,Dha_k,Ma_t,Ma,Dha_k,Ma_t]

def alarm():
    messagebox.showinfo("Alarm Notification","Alarm has been Set..")
    while True:
        if hour_var.get()==datetime.datetime.now().hour and min_var.get()==datetime.datetime.now().minute:
            # for j in range(2):
            #     for i in song_list:
            #         winsound.Beep(int(i),1000)
            # break
            print("Alarm Sound")



submit=ttk.Button(wn,text="Set Alarm",command=alarm)
submit.grid(row=2,column=1)

wn.mainloop()