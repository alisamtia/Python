from tkinter import *
wn=Tk()
wn.title("Canvas Title")
canvas=Canvas(wn,width=1000,height=1000,bg="red")
canvas.pack()
# canvas.create_text(x,y,text="Ali",font="arial bold",fill="yellow")
# y=Height
# x=width
canvas.create_text(500,40,text="Hello My Name is Muhammad Ali",font=("arial",20,"bold"),fill="yellow")
canvas.create_line(0,0,1000,1000,fill="white",width=4)
canvas.create_rectangle(0,0,100,500,fill="blue")
canvas.create_oval(200,200,120,330,fill="black")
canvas.create_arc(300,110,500,600,extent=70)
a=[250,110,480,200,280,280,250,110]
canvas.create_polygon(a,fill="blue",outline="gold",width=5)
canvas.pack()

im=PhotoImage(file="test.png")
canvas.create_image(0,0,image=im,anchor=NW)

wn.mainloop()