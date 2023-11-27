from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mg

wn=Tk()
wn.title("My Calculator")
wn.geometry("361x381+500+200")
wn.resizable(0,0)
dis=StringVar()
display=Entry(wn,font=("arial",20),border=29,background="powder blue",justify="right",textvariable=dis)
display.grid(row=0,columnspan=4)

ns=""
def num(n):
    global ns
    ns=ns+str(n)
    dis.set(ns)


btn1=Button(wn,text="1",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(1))
btn1.grid(row=1,column=0)

btn2=Button(wn,text="2",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(2))
btn2.grid(row=1,column=1)

btn3=Button(wn,text="3",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(3))
btn3.grid(row=1,column=2)

btn_add=Button(wn,text="+",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num('+'))
btn_add.grid(row=1,column=3)

btn4=Button(wn,text="4",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(4))
btn4.grid(row=2,column=0)

btn5=Button(wn,text="5",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(5))
btn5.grid(row=2,column=1)

btn6=Button(wn,text="6",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(6))
btn6.grid(row=2,column=2)

btn_min=Button(wn,text="-",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num('-'))
btn_min.grid(row=2,column=3)

btn7=Button(wn,text="7",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(7))
btn7.grid(row=3,column=0)

btn8=Button(wn,text="8",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(8))
btn8.grid(row=3,column=1)

btn9=Button(wn,text="9",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(9))
btn9.grid(row=3,column=2)

btn_mul=Button(wn,text="x",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num('*'))
btn_mul.grid(row=3,column=3)


# Last row

def btnc():
    dis.set("")

btnc=Button(wn,text="C",width=6,height=2,font=("arial",12,"bold"),bd=12,command=btnc)
btnc.grid(row=4,column=0)

btn0=Button(wn,text="0",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num(0))
btn0.grid(row=4,column=1)

btn_divi=Button(wn,text="/",width=6,height=2,font=("arial",12,"bold"),bd=12,command=lambda:num('/'))
btn_divi.grid(row=4,column=2)

def equ():
    global ns
    try:
        r=str(eval(ns))
    except:
        mg.showerror("Enter a Valid Value","Please only Numbers and Symbols of Calcualation")
    else:
        dis.set(r)

btn_equal=Button(wn,text="=",width=6,height=2,font=("arial",12,"bold"),bd=12,command=equ)
btn_equal.grid(row=4,column=3)



mainloop()