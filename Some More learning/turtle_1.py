# 0,0 upper left corner

# x >> Width
# y >> Height

from turtle import *
t=Turtle()
wn=Screen()
wn.title("Muhammad ali")
wn.bgcolor("yellow")
# BG Pic
# wn.bgpic("test.gif")

# Shapes: "arrow","turtle","circle","square","triangle","classic"
t.shape("turtle")
# Turtle Color
t.color("red","green")
# t.hideturtle()
t.speed(1)
t.begin_fill()


# t.forward(100)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(50)


for i in range(1,5):
    t.left(90)
    t.forward(50)

t.penup()
t.forward(100)
t.pendown()

for i in range(1,5):
    t.left(90)
    t.forward(50)

t.end_fill()


done()