from tkinter import ttk
import tkinter as tk

win=tk.Tk()
win.title('Tabs')

nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='ONE')
nb.add(page2,text='TWO')
# nb.grid(row=0,column=0) # Not good option
nb.pack(expand=True,fill='both')


labels=['Name','Age','Email','Gender','Country','State','City']

for i in range(len(labels)):
    # padx(Left and Right) pady(Top and bottom)
    a=tk.Label(page1,text=labels[i]+': ')
    a.grid(row=i,column=0,sticky=tk.W,padx=2,pady=2)

name_var=tk.StringVar()
dict_var={
    'Name':tk.StringVar(),
    'Age':tk.StringVar(),
    'Email':tk.StringVar(),
    'Gender':tk.StringVar(),
    'Country':tk.StringVar(),
    'State':tk.StringVar(),
    'City':tk.StringVar(),
}
a=0
for i in dict_var:
    cur_entry_box='entry'+str(i)
    cur_entry_box=ttk.Entry(page1,width=16,textvariable=dict_var[i])
    cur_entry_box.grid(row=a,column=1)
    a+=1

def ali():
    for i in dict_var:
        print(f'{i}:{dict_var[i].get()}')


name=ttk.Label(page2,text='Enter your Name: ')
# grid,pack
name.grid(row=0,column=0,sticky=tk.W)


age=ttk.Label(page2,text='Enter your Age: ')
age.grid(row=1,column=0,sticky=tk.W)

email=ttk.Label(page2,text="Enter your Email: ")
email.grid(row=2,column=0,sticky=tk.W)

email=ttk.Label(page2,text="Select Your Gender: ")
email.grid(row=3,column=0,sticky=tk.W)

# Create entry box
name_var=tk.StringVar()
name_entry_box=ttk.Entry(page2,width=16,textvariable=name_var)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()

email_var=tk.StringVar()
email_entry_box=ttk.Entry(page2,width=16,textvariable=email_var)
email_entry_box.grid(row=1,column=1)

age_var=tk.StringVar()
age_entry_box=ttk.Entry(page2,width=16,textvariable=age_var)
age_entry_box.grid(row=2,column=1)

# Create Combobox
gender_var=tk.StringVar()
gender_z=ttk.Combobox(page2,width=13,textvariable=gender_var,state='readonly')
gender_z['values']=('Male','Female','Other')
gender_z.current(0)
gender_z.grid(row=3,column=1)

# Create Radio button
hobbie=tk.StringVar()
work_entry=ttk.Radiobutton(page2,text="Student",value="Student",variable=hobbie)
work_entry.grid(row=4,column=0)

work_entry2=ttk.Radiobutton(page2,text="Teacher",value="Teacher",variable=hobbie)
work_entry2.grid(row=4,column=1)

# check Button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(page2,text="Check if You want to Subscribe out News Letter",variable=checkbtn_var)
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

    name_entry_box.delete(0,tk.END)
    age_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
    # Change color after Clear forground,background
    # use your own color Use any rgb Color
    # We cannot change color in ttk
    name.configure(foreground='#FBBC05')

button=ttk.Button(page1,text="Submit",command=action)
button.grid(row=7,column=0)

# Create Button
button=ttk.Button(page2,text="Submit",command=action)
button.grid(row=7,column=0)

win.mainloop()