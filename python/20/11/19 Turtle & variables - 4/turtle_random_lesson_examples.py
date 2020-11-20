import turtle
import random


###Example 1
##number = random.randrange(100, 1001, 100)
##print(number) 


###Example 2
##
##world = turtle.Screen( )
##world.setup(width=400, height=400)
##world.setworldcoordinates(0, 0, 400, 400)
##world.colormode(255)
##
##c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
##world.bgcolor(c)
##


###Example 3
##
##world = turtle.Screen()
##world.setup(width=400, height=400)
##world.setworldcoordinates(0,0,400,400)
##world.colormode(255)
##
##r = random.randint(100, 255)
##g = random.randint(100, 255)
##b = random.randint(100, 255)
##world.bgcolor((r, g, b))
##
##
##tula = turtle.Turtle()
##tula.up()
##tula.goto(250, 100)
##tula.down()
##
##c = (r, g, b)
##rgb_colour = f'{c}'
##tula.write(rgb_colour, font=("Arial", 20, "bold"))
##
##tula.up()
##tula.goto(250, 50)
##tula.down()
##
##hex_colour = f'#{r:x}{g:x}{b:x}'
##tula.write(hex_colour, font=("Arial", 20, "bold"))
##




###Example 4
##world = turtle.Screen()
##world.setup(width=400, height=400)
##world.setworldcoordinates(0,0,400,400)
##
##all_words = ['poem', 'creep', 'trick', 'frog', 'amuse', 'trait']
##
##tula = turtle.Turtle()
##tula.up()
##x = random.randrange(0, 301, 100)
##y = random.randrange(0, 301, 100)
##tula.goto(x, y)
##tula.down()
##
##word = random.choice(all_words)
##tula.write(word, font=("Arial", 40))
##
##tula.up()
##tula.home()




###Example 5
##world = turtle.Screen()
##world.setup(width=400, height=400)
##world.setworldcoordinates(0,0,400,400)
##world.colormode(255)
##c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
##world.bgcolor(c)
##
##
##title = "Turtle Options"
##print(title)
##print("-"*len(title))
##print("arrow, turtle, circle, square, triangle, classic")
##
##user_shape = input("\nEnter the shape you would like to use")
##
##tula = turtle.Turtle()
##tula.color("white", "black")
##tula.up()
##tula.goto(250, 100)
##tula.down()
##tula.shape(user_shape)
##tula.stamp()
##
##tula.up()
##tula.home()

                     
