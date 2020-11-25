import turtle

global turt

world = turtle.Screen()
world.setup(400, 400)
world.setworldcoordinates(0, 400, 400, 0)

def on_click(clickX, clickY):
	global turt
	angle = turt.towards(clickX, clickY)
	# dist = turt.distance(clickX, clickY)
	turt.setheading(angle)
	# turt.forward(dist)
	turt.goto(clickX, clickY)

print("t")
global turt
turt = turtle.Turtle()
world.onclick(on_click)
world.mainloop()
