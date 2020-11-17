import turtle
from time import sleep

def goto(x,y):
	turt.penup()
	turt.goto(x,y)
	turt.pendown()

def rect(x,y,w,h):
	goto(x,y)
	turt.begin_fill()
	turt.setheading(0)
	turt.forward(w)
	turt.setheading(90)
	turt.forward(h)
	turt.setheading(180)
	turt.forward(w)
	turt.setheading(270)
	turt.forward(h)
	turt.end_fill()

world = turtle.Screen()
world.setup(width=400, height=400)
world.setworldcoordinates(0,400,400,0)
world.bgcolor("#FFFFFF")
#name your turtle
turt = turtle.Turtle()

turt.color("green")
rect(50,100,100,200)
turt.color("yellow")
rect(150,100,100,200)
turt.color("red")
rect(250,100,100,200)

sleep(5)