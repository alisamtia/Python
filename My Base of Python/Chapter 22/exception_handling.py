import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box


win = tk.Tk()
win.title('Exception Handling')

item_frame=ttk.LabelFrame(win,text="Enter Your Details Below: ")
item_frame.grid(row=0,column=0,padx=10)

# Labels
name_label=ttk.Label(item_frame,text='Enter your Name: ',font=('arial',14))
name_label.grid(row=0,column=0)

age_label=ttk.Label(item_frame,text='Enter your Age: ',font=('arial',14))
age_label.grid(row=0,column=1)

# entryies
name_var=tk.StringVar()
name=ttk.Entry(item_frame,width=25,textvariable=name_var)
name.grid(row=1,column=0,padx=3)


age_var=tk.StringVar()
age=ttk.Entry(item_frame,width=25,textvariable=age_var)
age.grid(row=1,column=1)

def submit():
    # m_box.showerror('Title','This is Error')
    # m_box.showinfo('Title','This is info exception')
    # m_box.showwarning('Title','This is info Warning')
    name=name_var.get()
    age=age_var.get()
    if name=='' or age=='':
        m_box.showerror('Fill Details','Please Fill Age and name Both Thank YOU!')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Enter Valid Value','Please only enter the Numbers in Age!!')
        else:
            if age<10:
                m_box.showwarning('Warning','You are not 10, You can see this movie at your own risk.')
            print(f'{name}:{age}')

btn=ttk.Button(item_frame,text='Submit',command=submit)
btn.grid(columnspan=2,row=3)

win.mainloop()