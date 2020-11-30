from math import degrees, sin, atan # I could import all but that might cause issues
import turtle

# Functions & Turtle - Exercise #3 (Snowman⛄)

def goto(a_turtle,x,y):
	a_turtle.up()
	a_turtle.goto(x, y)
	a_turtle.down()

def draw_filled_circle(a_turtle, x, y, radius):
	goto(a_turtle, x, y)
	a_turtle.dot(radius*2)

def draw_triangle(a_turtle, x, y, side_a, side_b):
	angleRad = atan(side_b/side_a)
	angleDeg = degrees(angleRad)
	side_c = side_b/sin(angleRad) # Trig is really useful

	goto(a_turtle, x, y)
	a_turtle.setheading(270)
	a_turtle.forward(side_a)
	a_turtle.left(90)
	a_turtle.forward(side_b)
	a_turtle.left(90+angleDeg)
	a_turtle.forward(side_c)

def fillRect(a_turtle, x, y, w, h, angle=0): # This is not great but it works for this 😅
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

	a_turtle.color("#A06010") # Brown
	fillRect(a_turtle, x+r, y, 10, 150, -30)
	fillRect(a_turtle, x-r, y, 10, 150, 180+30)

# Main

# Functions & Turtle - Exercise #3 (Snowman⛄)

world = turtle.Screen()
world.setup(400, 400)
world.setworldcoordinates(0,400,400,0)
world.bgcolor("#808080") # Darker gray

turt = turtle.Turtle()

draw_snowman(turt, 200,200)

world.mainloop() # Keep the window open so we can see our beautiful ⛄