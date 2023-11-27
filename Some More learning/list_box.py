from tkinter import ttk
from tkinter import *
wn=Tk()
wn.title("List BOX")
wn.geometry("400x500")

l=Listbox(wn,width=50,height=10,selectmode=SINGLE) #EXTENDED,MULTIPLE,SINGLE
l.insert(1,"Python")
l.insert(2,"PHP")
l.insert(3,"HTML")
l.insert(4,"CSS")
l.insert(5,"JavaScript")
l.pack()

def print_h():
    data=l.curselection()
    print(data)
    for i in data:
        print(l.get(i))

def delete_data():
    a=l.curselection()
    for i in a:
        print(l.delete(i))



s=ttk.Button(wn,text="Print Here",command=print_h)
s.pack()

btn2=ttk.Button(wn,text="Delete Selected Item",command=delete_data)
btn2.pack()



mainloop()