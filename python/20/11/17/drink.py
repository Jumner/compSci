import turtle
from time import sleep

def goto(x,y):
	t.penup()
	t.goto(x,y)
	t.pendown()

def rect(x,y,w,h):
	goto(x,y)
	t.begin_fill()
	t.setheading(0)
	t.forward(w)
	t.setheading(90)
	t.forward(h)
	t.setheading(180)
	t.forward(w)
	t.setheading(270)
	t.forward(h)
	t.end_fill()

world = turtle.Screen()
world.setup(width=400, height=400)
world.setworldcoordinates(0,400,400,0)
world.bgcolor("#A0E0FF")
#name your tle
t = turtle.Turtle()
t.speed(0)

t.color("#FFFFFF")
rect(125,75,150,250)
t.color("#FFD050")
rect(135,125,130,190)
t.color("#FFFFFF")
rect(145,135,25,25)
rect(185,170,15,15)
t.color("#FF0000")
rect(230,30,50,10)
rect(230,30,10,275)

sleep(5)