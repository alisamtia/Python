from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import time

wn=Tk()

bar=Progressbar(wn,orient=HORIZONTAL,length=400)
bar.pack(padx=20,pady=20)

def start1():
    work=100
    download=0
    speed=1
    while download<work:
        time.sleep(0.05)
        bar['value']+=(speed/work)*100
        download+=speed
        a.set(str(int(download/work)*100)+"%")
        task.set(f"{download}/{(download/work)*100} GB Work Completed")
        wn.update_idletasks()

a=StringVar()
percent=Label(wn,textvariable=a)
percent.pack()

task=StringVar()
pa=Label(wn,textvariable=task)
pa.pack()

btn=ttk.Button(wn,text="Download",command=start1)
btn.pack()

wn.geometry("400x400+200+200")
wn.mainloop()