from tkinter import ttk
import tkinter as tk
win=tk.Tk()
win.title('Label Frame')

label_frame=tk.LabelFrame(win,text='Enter Your Details Below: ')
label_frame.grid(row=0,column=0,padx=10)

labels=['Name','Age','Email','Gender','Country','State','City']

for i in range(len(labels)):
    # padx(Left and Right) pady(Top and bottom)
    a=tk.Label(label_frame,text=labels[i]+': ')
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
    cur_entry_box=ttk.Entry(label_frame,width=16,textvariable=dict_var[i])
    cur_entry_box.grid(row=a,column=1)
    a+=1

def ali():
    for i in dict_var:
        print(f'{i}:{dict_var[i].get()}')

btn=ttk.Button(win,text='Submit',command=ali)
btn.grid(row=7,columnspan=2)


for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)

win.mainloop()