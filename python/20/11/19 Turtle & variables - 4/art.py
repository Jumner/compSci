import turtle, random
from colorsys import hsv_to_rgb # Because I am not doing that ever again
from multiprocessing.pool import ThreadPool # Oh boy here we go! 😨
from datetime import datetime

howManyTurtles = 50 # Hell yeah we want them turtles
iterations = 1000 # Hell yeah, them turtles go far!

size = 400
center = size/2
lineWidth = 1

world = turtle.Screen() # Create the screen
world.setup(width=size+20, height=size+20) # Setup with size 400 x 400
world.setworldcoordinates(0,size,size,0) # Set it so 0,0 is top left
world.bgcolor("#FFFFFF") # Clear it and set the bg back to white

turtles = [] # Make an list of turtles 😄
for i in range(howManyTurtles): # Run for each turtle
	turtles.append(turtle.Turtle()) # Make two turtles
	turtles[i].color(hsv_to_rgb(i/howManyTurtles,1,1))

for t in turtles: # Set them up
	t.speed(10)
	t.width(lineWidth) # Width of their lines
	t.penup() # Pick up the pen and move to random spot
	# t.goto(random.randint(0,400), random.randint(0,400)) # Goto a random spot
	t.goto(center,center) # Start in the center for circles
	t.pendown() # Put the pen down to draw
	t.setheading(random.randint(0,360)) # Look in a random direction
	t.speed('fastest') # Ok now we want to go "fast"


for t in turtles:
	t.hideturtle() # Hides them and speeds it all up
	# This is separate purely for fashion

turtle.tracer(0,0)

def calcMove(t):
	if t.distance(center,center) >= center: # If it is too far
	# pos = t.pos()
	# if abs(200-pos[0]) >= 200 or abs(200-pos[1]) >= 200: # If it is too far
		return (t.towards(center,center) + random.uniform(-30,30)) - t.heading()
	return random.uniform(-30,30)
	
def doMove(t,o):
	t.right(o)
	t.forward(1)
	return t

pool = ThreadPool(processes=howManyTurtles)
for i in range(iterations): # How many pixels each turtle should travel
	out = pool.map_async(calcMove,turtles)
	turtles = list(map(doMove,turtles,out.get()))

	world.title(f'{100*(i+1)/iterations}% Done') # And set the title
	turtle.update() # Unindent this for speed, indent for satifcaction

input("done") # Wait to not lose the beautiful image