from tkinter import *
import tkinter as tk
import time
import random

wn=Tk()
wn.title("Animation Python part 1")
canvas=Canvas()
canvas.pack(fill=tk.BOTH,expand=True)
wn.geometry("800x600")

class Ball:
    def __init__(self,color,size):
        self.ball=canvas.create_oval(10,10,size,size,fill=color)
        self.x=random.randrange(1,8)
        self.y=random.randrange(1,8)
    
    def animate(self):
        canvas.move(self.ball,self.x,self.y)
        self.pos=canvas.coords(self.ball)
        if self.pos[3]>=600 or self.pos[1] <= 0:
            self.y=-self.y
        elif self.pos[2]>=800 or self.pos[0] <= 0:
            self.x=-self.x
        else:
            pass

m_ball=[]
colors=["red","blue","grey","gold","purple","yellow","sky blue","orange","green"]
for i in range(200):
    m_ball.append(Ball(random.choice(colors),50))

while True:
    for i in m_ball:
        i.animate()
    wn.update()
    time.sleep(0.01)


mainloop()