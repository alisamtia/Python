from tkinter import *
from tkinter import ttk

wn=Tk()

wn.title("Animated Text")
wn.geometry("1000x100")

count=0
slider_text=''
def slider():
    global count,slider_text
    text="Hey, There My name is Muhammad Ali. I am 12 Years OLD."
    if count>=len(text):
        count=0
        slider_text=''
    slider_text+=text[count]
    count=count+1
    label1.configure(text=slider_text)
    label1.after(250,slider)
    
label1=ttk.Label(text=slider_text,font=("Comic Sans MS",18),foreground="red",background="yellow")
label1.pack()

slider()
wn.mainloop()