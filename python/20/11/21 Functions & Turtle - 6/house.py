import turtle
import random
from time import sleep
from math import atan, sin, degrees

def goto(a_turtle,x,y):
	a_turtle.up()
	a_turtle.goto(x, y)
	a_turtle.down()

def draw_circle(a_turtle, x, y, radius):
	goto(a_turtle, x, y-radius)
	a_turtle.circle(radius)

def draw_filled_circle(a_turtle, x, y, radius):
	goto(a_turtle, x, y)
	a_turtle.dot(radius*2)

def draw_triangle(a_turtle, x, y, side_a, side_b):
	angleRad = atan(side_b/side_a)
	angleDeg = degrees(angleRad)
	side_c = side_b/sin(angleRad)
	print(f'A side length: {side_a:.1f}')
	print(f'B side length: {side_b:.1f}')
	print(f'C side length: {side_c:.1f}')
	print(f'Turning angle: {angleDeg:.1f}')

	goto(a_turtle, x, y)
	a_turtle.setheading(270)
	a_turtle.forward(side_a)
	a_turtle.left(90)
	a_turtle.forward(side_b)
	a_turtle.left(90+angleDeg)
	a_turtle.forward(side_c)

def fillRect(a_turtle, x, y, w, h, angle=270):
	goto(a_turtle, x, y)
	a_turtle.setheading(angle)
	a_turtle.begin_fill()
	a_turtle.forward(h)
	a_turtle.left(90)
	a_turtle.forward(w)
	a_turtle.left(90)
	a_turtle.forward(h)
	a_turtle.left(90)
	a_turtle.forward(w)
	a_turtle.end_fill()

def draw_snowman(a_turtle, x, y):
	r = 50
	dif=20
	a_turtle.color("#F0F0F0") # Light gray
	draw_filled_circle(a_turtle,x,y-(r+(r-dif)),r-dif)
	draw_filled_circle(a_turtle,x,y,r)
	draw_filled_circle(a_turtle,x,y+(r+(r+dif)),r+dif)

	a_turtle.color("#303030") # Near black
	draw_filled_circle(a_turtle,x,y,8)
	draw_filled_circle(a_turtle,x,y-20,8)
	draw_filled_circle(a_turtle,x,y+20,8)

	draw_filled_circle(a_turtle,x+15,y-(r+(15+r-dif)),10)
	draw_filled_circle(a_turtle,x-15,y-(r+(15+r-dif)),10)

	a_turtle.color("#FF8030") # Carrot orange
	a_turtle.begin_fill()
	draw_triangle(a_turtle,x-3,20+y-(r+(r-dif)),25,6)
	a_turtle.end_fill()

	a_turtle.color("#A06010")
	fillRect(a_turtle, x+r, y, 10, 150, -30)
	fillRect(a_turtle, x-r, y, 10, 150, 180+30)

def drawWindow(t, x, y, w, h):
	t.color("#D0D0FF")
	fillRect(t,x+w/2,y+h/2,w,h)
	# t.color("#F0F0F0")

def drawHouse(t, x, y):
	t.color("#C0C0C0")
	fillRect(t, x,y,200,100)
	t.color("#D0A090")
	t.begin_fill()
	draw_triangle(t, x-10,y-175,-75,220)
	t.end_fill()
	drawWindow(t, x-10,y-130,30,30)
	drawWindow(t, x,y-50, 50, 50)
	drawWindow(t, x+120,y-50, 50, 50)
	t.color("#606060")
	fillRect(t,x+100,y,20,50)
	# drawWindow(t, x+20,y-25, 50, 50)

world = turtle.Screen()
world.setup(400, 400)
world.setworldcoordinates(0,400,400,0)
world.bgcolor("#FFFFFF")
turt = turtle.Turtle()

drawHouse(turt, 100, 300)

sleep(10)