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

world = turtle.Screen()
world.setup(400, 400)
world.setworldcoordinates(0,400,400,0)
world.bgcolor("#FFFFFF")
turt = turtle.Turtle()

turt.color("#5010C0")
draw_circle(turt, 200, 200, 50)
draw_filled_circle(turt, 200, 200, 30)
sleep(1)

world.clear()

turt = turtle.Turtle()

# a = float(input("Enter side length a"))
# b = float(input("Enter side length b"))
a = 200
b = 80

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

turt.color("#1040FF")
draw_triangle(turt,100,200,200,80)
sleep(1)

def fillRect(a_turtle, x, y, w, h, angle=0):
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

world.clear()
world.bgcolor("#808080") # Darker gray

turt = turtle.Turtle()

draw_snowman(turt, 200,200)

sleep(1)



sleep(10)