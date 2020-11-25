import turtle
from time import sleep

world = turtle.Screen()
world.setup(400, 400)
world.setworldcoordinates(0, 400, 400, 0)
turt = turtle.Turtle()
# user_choice = world.textinput("Window name", "Window text")
# print(user_choice)

def goto(a_turtle, x, y):
	a_turtle.up()
	a_turtle.goto(x,y)
	a_turtle.down()

def draw_filled_circle(a_turtle, x, y, radius):
	goto(a_turtle, x, y)
	a_turtle.dot(radius*2)

def draw_dots(mouseX, mouseY):
	sections = 8
	sectionSize = 400/sections
	section = 1 + mouseY//sectionSize # 0-3
	c = 1-(mouseY/400)
	turt.color(1, 0.3+c*0.7, c)
	draw_filled_circle(turt, mouseX, mouseY, (section*50)/sections)
	print(section)

world.onclick(draw_dots)
world.mainloop()