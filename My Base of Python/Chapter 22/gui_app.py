# python tkinter tutorial
# tee-kinter,tk-inter,kinter

# starter code
# import tkinter
# from tkinter import *
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win =tk.Tk()
win.title('Ali Softs')
# ------------------> label,button,rado button etc - tk(simple),ttk(Professtional)
name=ttk.Label(win,text='Enter your Name: ')
# grid,pack
name.grid(row=0,column=0,sticky=tk.W)


age=ttk.Label(win,text='Enter your Age: ')
age.grid(row=1,column=0,sticky=tk.W)

email=ttk.Label(win,text="Enter your Email: ")
email.grid(row=2,column=0,sticky=tk.W)

email=ttk.Label(win,text="Select Your Gender: ")
email.grid(row=3,column=0,sticky=tk.W)

# Create entry box
name_var=tk.StringVar()
name_entry_box=ttk.Entry(win,width=16,textvariable=name_var)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()

email_var=tk.StringVar()
email_entry_box=ttk.Entry(win,width=16,textvariable=email_var)
email_entry_box.grid(row=1,column=1)

age_var=tk.StringVar()
age_entry_box=ttk.Entry(win,width=16,textvariable=age_var)
age_entry_box.grid(row=2,column=1)

# Create Combobox
gender_var=tk.StringVar()
gender_z=ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_z['values']=('Male','Female','Other')
gender_z.current(0)
gender_z.grid(row=3,column=1)

# Create Radio button
hobbie=tk.StringVar()
work_entry=ttk.Radiobutton(win,text="Student",value="Student",variable=hobbie)
work_entry.grid(row=4,column=0)

work_entry2=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=hobbie)
work_entry2.grid(row=4,column=1)

# check Button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text="Check if You want to Subscribe out News Letter",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

def action():
    username=name_var.get()
    useremail=email_var.get()
    userage=age_var.get()
    gender=gender_var.get()
    userhobbie=hobbie.get()
    subscribe=checkbtn_var.get()
    if subscribe==0:
        subscribed='No'
    else:
        subscribed='Yes'
    # with open('file.txt','a', newline='') as f:
    #     f.writelines(f'\n{username},{userage},{useremail},{gender},{userhobbie},{subscribed}')
    with open('file.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['Username','UserEmail','User Age','User Gender','User Type','Subscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Username':username,
            'UserEmail':useremail,
            'User Age':userage,
            'User Gender':gender,
            'User Type':userhobbie,
            'Subscribed':subscribed
        })

    name_entry_box.delete(0,tk.END)
    age_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
    # Change color after Clear forground,background
    # use your own color Use any rgb Color
    # We cannot change color in ttk
    name.configure(foreground='#FBBC05')


# Create Button
button=ttk.Button(win,text="Submit",command=action)
button.grid(row=7,column=0)

win.mainloop()