import turtle # Use the turtle library
from time import sleep # to keep the window open

def goto(x,y): # Goto a certain position without leaving a trail
	turt.penup()
	turt.goto(x,y)
	turt.pendown()

def rect(x,y,w,h): # Draw a rect from xy with wh
	goto(x,y) # Goto the start of the rect
	turt.setheading(0) # Set it to the right angle
	turt.begin_fill() # Start the fill
	turt.forward(w) # Go the width
	turt.left(90) # Turn
	turt.forward(h)
	turt.left(90)
	turt.forward(w)
	turt.left(90)
	turt.forward(h)
	turt.end_fill() # End fill

world = turtle.Screen() # Create the screen
world.setup(width=400, height=400) # Setup with size 400 x 400
world.setworldcoordinates(0,400,400,0) # Set it so 0,0 is top left
world.bgcolor("#FFFFFF") # Set bg color to white
#name your turtle
turt = turtle.Turtle() # Create the turtle
turt.color("black") # Draw in black

rect(50,50,40,40) # Draw rects
rect(125,125,75,75)
rect(200,200,75,75)
rect(275,275,75,75)

rect(100,50,200,40)
rect(50,100,40,200)

sleep(5) # Wait 5 secs