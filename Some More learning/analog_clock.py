from turtle import *
import time
time.time()
t=Turtle()
wn=Screen()
wn.title("Simple Analog Clock")
wn.bgcolor('black')
wn.setup(600,600)
t.speed(1)
t.pensize(3) #Width of things
t.hideturtle() #Hide turtule
wn.tracer(0)

def draw_clock(h,m,s,t):
    t.penup()
    t.goto(0,210)
    t.setheading(180)
    t.pencolor('green')
    t.pendown()
    t.circle(210)
    # Draw Clock MArkng for minutes and seconds
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for i in range(12):
        t.forward(190)
        t.pendown()
        t.fd(20) # Forward Short CUT
        t.penup()
        t.goto(0,0)
        t.right(30)

    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for i in range(60):
        t.forward(200)
        t.pendown()
        t.fd(10) # Forward Short CUT
        t.penup()
        t.goto(0,0)
        t.right(6)
    # draw Numbers on clock
    def count(a,b,c,number):
        t.penup()
        t.goto(0,0)
        t.setheading(a)
        t.fd(b)
        t.setheading(0)
        t.fd(c)
        t.write(number,move=False,align='center',font=("arial",25,"normal"))
    
    count(60,145,15,1)
    count(30,135,35,2)
    count(352,150,25,3)
    count(315,150,45,4)
    count(290,178,25,5)
    count(270,190,0,6)
    count(233,210,48,7)
    count(208,220,45,8)
    count(185,200,25,9)
    count(156,185,25,10)
    count(130,157,15,11)
    count(108,160,48,12)

    # Draw Hours 
    t.pu
    t.goto(0,0)
    t.pencolor('red')
    t.setheading(90)
    angle=(h/12)*360
    t.right(angle)
    t.pendown()
    t.fd(80)

    
    # Minutes Hours 
    t.pu
    t.goto(0,0)
    t.pencolor('blue')
    t.setheading(90)
    angle=(m/60)*360
    t.right(angle)
    t.pendown()
    t.fd(120)

    
    # Draw Seconds
    t.pu
    t.goto(0,0)
    t.pencolor('yellow')
    t.setheading(90)
    angle=(s/60)*360
    t.right(angle)
    t.pendown()
    t.fd(160)
    
    # Design by
    t.penup()
    t.setheading(0) 
    t.goto(0,-120)#Height
    t.fd(10) #widht
    t.setheading(0)
    t.fd(-1)
    t.write("Designed By: Muhammad Ali",move=False,align='center',font=("arial",12,"normal"))

    # Website
    t.penup()
    t.setheading(0) 
    t.goto(0,100)#Height
    t.fd(10) #widht
    t.setheading(0)
    t.fd(-1)
    t.write("WWW.CATVIDSHD.COM",move=False,align='center',font=("arial",12,"normal"))

while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    draw_clock(h,m,s,t)
    wn.update()
    time.sleep(1)
    t.clear()



mainloop()