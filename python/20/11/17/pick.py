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
turt.color("black")

rect(50,50,40,40)
rect(125,125,75,75)
rect(200,200,75,75)
rect(275,275,75,75)

rect(100,50,200,40)
rect(50,100,40,200)

sleep(5)