from tkinter import *
import tkinter as tk
import time

wn=Tk()
wn.title("Animation Python part 1")
canvas=Canvas()
canvas.pack(fill=tk.BOTH,expand=True)
wn.geometry("800x600")

ball=canvas.create_oval(10,10,60,60,fill="red")

# for i in range(400):
#     canvas.move(ball,1,2)
#     canvas.update()
#     time.sleep(0.00010)

x=1
y=2
while True:
    canvas.move(ball,x,y)
    pos=canvas.coords(ball)
    # [left top right bottom]
    # print(pos)
    if pos[3]>=600 or pos[1] <= 0:
        y=-y
    elif pos[2]>=800 or pos[0] <= 0:
        x=-x
    else:
        pass
    canvas.update()
    time.sleep(0.01)

mainloop()