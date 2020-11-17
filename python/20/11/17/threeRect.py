import turtle
from time import sleep

def goto(x,y):
	turt.penup()
	turt.goto(x,y)
	turt.pendown()

def rect(x,y,w,h):
	goto(x,y)
	turt.setheading(0)
	turt.begin_fill()
	turt.forward(w)
	turt.right(90)
	turt.forward(h)
	turt.right(90)
	turt.forward(w)
	turt.right(90)
	turt.forward(h)
	turt.end_fill()

world = turtle.Screen()
world.setup(width=400, height=400)
world.setworldcoordinates(0,0,400,400)
world.bgcolor("#FFFFFF")
#name your turtle
turt = turtle.Turtle()
turt.color("black")

rect(0,200,100,200)

rect(100,400,300,200)

rect(200,100,200,100)

sleep(5)

