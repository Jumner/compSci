import random
import turtle
from time import sleep
from colorsys import hsv_to_rgb # Because I am not doing that ever again
from multiprocessing.pool import ThreadPool # Oh boy here we go! 😨

random.seed() # Set seed to time

def goto(x,y): # Goto a certain position without leaving a trail
	turt.penup()
	turt.goto(x,y)
	turt.pendown()

def makeCircle(rad, x=-1, y=-1, col=-1):
	c = random.randint(0,1)
	turt.color(c,c,c)
	if x == -1 and y == -1 and col == -1:
		x = random.randrange(rad, 400-rad)
		y = random.randrange(rad, 400-rad)
		turt.color(random.random(), random.random(), random.random())
	goto(x,y)
	turt.dot(rad)

def rect(x,y,w,h): # Draw a rect from xy with wh
	goto(x,y) # Goto the start of the rect
	turt.setheading(0) # Set it to the right angle
	turt.begin_fill() # Start the fill
	turt.forward(w) # Go the width
	turt.setheading(90) # Setting it instead of turning did not fix 😿
	turt.forward(h)
	turt.setheading(180)
	turt.forward(w)
	turt.setheading(270)
	turt.forward(h)
	turt.end_fill() # End fill

print("Random Number Generator\n-----------------------\n\n")
low = int(input("Enter a low value"))
high = int(input("Enter a high value"))

print(f'\nYour number is: {random.randint(low,high)}')

for i in range(3):
	print(random.randrange(1000,2000,50))

letters = "qwertyuiopasdfghjklzxcvbnm"
# (number in range 0-9)(letter)(letter)(number in range(80-99)(letter)
passWd = str(random.randint(0,9)) + random.choice(letters)*2 + str(random.randint(80,99)) + random.choice(letters)
print(passWd)


greetingList = ["hello", "salut", "hola", "ni hao", "ahlan"]
greetingList.append(greetingList[0])
greetingList.append(greetingList[3])
greetingList.append(greetingList[3])
greetingList.append(greetingList[4])
greetingList.append(greetingList[4])

print(random.choice(greetingList))

world = turtle.Screen() # Create the screen
world.setup(width=400, height=400) # Setup with size 400 x 400
world.setworldcoordinates(0,400,400,0) # Set it so 0,0 is top left
world.bgcolor("#FFFFFF") # Set bg color to white
#name your turtle
turt = turtle.Turtle() # Create the turtle

for i in range(10):
	makeCircle(50)

sleep(10) # Wow look at those circles!🤣

world.clear()
world.bgcolor("#000000") # Clear the screen and make it black

turt.color("#FFFFFF") # Draw in white
rect(95, 95, 210, 210) # Draw a rect
turt.color("#000000") # Draw in black
rect(100,100,200,200) # Draw a smaller rect to make the white border

makeCircle(50,150,140,0) # Draw the 6 circles
makeCircle(50,150,200,0)
makeCircle(50,150,260,0)
makeCircle(50,250,140,0)
makeCircle(50,250,200,0)
makeCircle(50,250,260,0)

sleep(10) # Wow look at THOSE circles!🙃

world.clear()
world.bgcolor("#FFFFFF") # Clear it and set the bg back to white

turtles = [] # Make an list of turtles 😄
howManyTurtles = 20 # Hell yeah we want them turtles
for i in range(howManyTurtles): # Run for each turtle
	turtles.append(turtle.Turtle()) # Make two turtles
	turtles[i].color(hsv_to_rgb(i/howManyTurtles,1,1))

for t in turtles: # Set them up
	t.speed(10)
	t.width(1) # Width of their lines
	t.penup() # Pick up the pen and move to random spot
	# t.goto(random.randint(0,400), random.randint(0,400)) # Goto a random spot
	t.goto(200,200) # Start in the center for circles
	t.pendown() # Put the pen down to draw
	t.setheading(random.randint(0,360)) # Look in a random direction
	t.speed(0) # Ok now we want to go "fast"
for t in turtles:
	t.hideturtle() # Hides them and speeds it all up
	# This is separate purely for fashion

def calcMove(t):
# 	pos = t.pos()
	if t.distance(200,200) >= 200: #abs(200-pos[0]) >= 200 or abs(200-pos[1]) >= 200: # If it is too far
		return (t.towards(200,200) + random.uniform(-30,30)) - t.heading()
	return random.uniform(-30,30)
	
def doMove(t,o):
	t.right(o)
	t.forward(1)
	return t

iterations = 1000
pool = ThreadPool(processes=howManyTurtles)
for i in range(iterations): # How many pixels each turtle should travel
	out = pool.map_async(calcMove,turtles)
	turtles = list(map(doMove,turtles,out.get()))

	world.title(f'{100*i/iterations}% Done') # And set the title
	# This is not as bad as it looks
	# Most of the time is spent on the turtles

input("done") # Wait to not lose the beautiful image