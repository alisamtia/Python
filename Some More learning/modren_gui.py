# pip install customtkinter
from customtkinter import *
wn=CTk()
wn.title("Modren GUI")
set_appearance_mode("dark") #Dark, system, Light
set_default_color_theme("green") #blue,green,dark-blue

frame=CTkFrame(wn)
frame.pack(padx=60,pady=20,expand=1,fill=BOTH)

label=CTkLabel(frame,text="Login Form",font=("Arial",25,"bold"))
label.pack(padx=10,pady=12)

l1=StringVar()
l2=StringVar()

username=CTkEntry(frame,placeholder_text="User Name",textvariable=l1)
username.pack(padx=10,pady=12)

password=CTkEntry(frame,placeholder_text="Password",show="*",placeholder_text_color="red",textvariable=l2)
password.pack(padx=10,pady=12)

def submit():
    print(l1.get())
    print(l2.get())

submit=CTkButton(frame,text="Login",command=submit)
submit.pack(padx=10,pady=12)


chk=CTkCheckBox(frame,text="Remeber ME")
chk.pack(padx=10,pady=12)

wn.geometry("400x400+120+120")
wn.mainloop()