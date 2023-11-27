import csv
import tkinter as tk
from tkinter import ttk
import pyttsx3


root=tk.Tk()
root.title("ali")

label1=tk.Label(root,text="Name: ")
label1.grid(row=0,column=0,padx=10,pady=7)

name_var=tk.StringVar()
name=ttk.Entry(root,text="Name",textvariable=name_var)
name.grid(row=0,column=1,padx=10,pady=7)



label2=tk.Label(root,text="Phone: ")
label2.grid(row=1,column=0,padx=10,pady=7)

phone_var=tk.StringVar()
phone=ttk.Entry(root,text="Phone: ",textvariable=phone_var)
phone.grid(row=1,column=1,padx=10,pady=7)

def act():
    global name_var
    global phone_var
    name_get=name_var.get()
    phone_get=phone_var.get()
    
    fieldnames = ['Name','Given Name','Additional Name','Family Name','Yomi Name','Given Name Yomi','Additional Name Yomi','Family Name Yomi','Name Prefix','Name Suffix','Initials','Nickname','Short Name','Maiden Name','Birthday','Gender','Location','Billing Information','Directory Server','Mileage','Occupation','Hobby','Sensitivity','Priority','Subject','Notes','Language','Photo','Group Membership','Phone 1 - Type','Phone 1 - Value','Organization 1 - Type','Organization 1 - Name','Organization 1 - Yomi Name','Organization 1 - Title','Organization 1 - Department','Organization 1 - Symbol','Organization 1 - Location','Organization 1 - Job Description']
    with open('a.csv', 'a', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'Name':name_get,
            'Given Name':name_get,
            'Phone 1 - Type':'* myContacts',
            'Phone 1 - Value':phone_get
        })
        engine = pyttsx3.init()
        engine.say(phone_get)
        engine.runAndWait()


submit=ttk.Button(root,text="Add",command=act)
submit.grid(row=2,columnspan=2)



root.mainloop()