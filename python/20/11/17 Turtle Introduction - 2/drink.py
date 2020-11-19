import turtle # Use the turtle library
from time import sleep # to keep the window open

def goto(x,y): # Goto a certain position without leaving a trail
	t.penup()
	t.goto(x,y)
	t.pendown()

def rect(x,y,w,h): # Draw a rect from xy with wh
	goto(x,y) # Goto the start of the rect
	t.setheading(0) # Set it to the right angle
	t.begin_fill() # Start the fill
	t.forward(w) # Go the width
	t.setheading(90) # Setting it instead of turning did not fix 😿
	t.forward(h)
	t.setheading(180)
	t.forward(w)
	t.setheading(270)
	t.forward(h)
	t.end_fill() # End fill

world = turtle.Screen() # Create the screen
world.setup(width=400, height=400) # Setup with size 400 x 400
world.setworldcoordinates(0,400,400,0) # Set it so 0,0 is top left
world.bgcolor("#A0E0FF") # Set bg color to blue
#name your turtle I named it t. Sorry not sorry
t = turtle.Turtle()

t.color("#FFFFFF") # Draw in white
rect(125,75,150,250) # Draw glass
t.color("#FFD050") # Draw in orange
rect(135,125,130,190) # Draw liquid
t.color("#FFFFFF")
rect(145,135,25,25) # Make bubbles
rect(185,170,15,15)
t.color("#FF0000") # Draw in red
rect(230,30,50,10) # Draw straw
rect(230,30,10,275)

sleep(5) # Wait 5 sec