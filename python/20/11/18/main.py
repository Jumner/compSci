from datetime import date
from math import pi
from numpy import mean

total = 20 + 32
print(total)

power = 5**2
print(power)

expression = (5+9) * (15-7)
print(expression)

hour = 9
minute =  10
hour -= 1
totalMinutes = hour*60 + minute
print(totalMinutes)

x = 2
y = x + x
print(y) # Adds integers

s = "2"
t = s + s
print(t) # Adds strings

# number = 462642 # Declares and defines number
# print(number + 5) # 'number' is not defined
# print(time().)

year_of_birth = int(input("Please enter your year of birth"))
print(date.today().year - year_of_birth)

r = 5
sphereVolume = (4/3)*(pi)*(r**3)
print(sphereVolume)

LYconversion = 5.878*10**12
distMiles = 2900000 * LYconversion # 2.9m ly
print(distMiles)

ageYears = 15000000000 # 15b years old
ageSec = ageYears * 365.2422 * 24 * 60 * 60
print(ageSec)

conversion_factor = 2.54
inches = int(input("Please enter the number of inches to convert to cm"))
# Causes error if you enter non integer
# This could be fixed with a try except block
centimeters = inches * conversion_factor
print(f'{inches} inches = {centimeters:.1f} cm')

conversion_factor = 2.54
while True: # What are you gonna do abt it? 😁
	try:	
		inches = int(input("Please enter the number of inches to convert to cm"))
		# Causes error if you enter non integer
		# Wow look at this code! It all works!
		centimeters = inches * conversion_factor
		print(f'{inches} inches = {centimeters:.1f} cm')
	except ValueError:
		print("Please enter an ingeger value such as 3 or 8")
	else:
		break # Just making sure I Never forget this

conversion_factor = 2.54
cm = int(input("Please enter the number of cm to convert to inches"))
# Causes error if you enter non integer
# This could be fixed with a try except block
inches = cm / conversion_factor
print(f'{cm} inches = {inches:.1f} cm')

lastName = input("Please enter your last name")
firstName = input("Please enter your first name")
print(f'{lastName}, {firstName}')

# numberOne = eval(input("Enter first number"))
# numberTwo = eval(input("Enter second number"))
numberOne = float(input("Enter first number")) # Use float bc eval is bad
numberTwo = float(input("Enter second number"))


numSum = numberOne + numberTwo
numDif = numberOne - numberTwo
numMul = numberOne * numberTwo
numAvg = mean([numberOne, numberTwo]) # Avg numbers using numpy :)
numMax = max(numberOne, numberTwo) # Max of numbers using max function

number = int(input("Enter and integer"))
remainder = number % 2
print(f'{number} has a remainder of {remainder} when divided by 2')
remainder = number % 5
print(f'{number} has a remainder of {remainder} when divided by 5')
remainder = number % 10
print(f'{number} has a remainder of {remainder} when divided by 10')

w = float(input("Enter the width of the rectangle"))
l = float(input("Enter the length of the rectangle"))
a = w*l
print(f'The area of the rectangle is {a}')

n=5
s="Hello"
t="World"

print(s+t)
print(s*n)
print('-'*20)
print('|'+'A'*18+'|')

x = 3 # Change the size later
y = 3
r1 = "+--"*x+"+"
r2 = "|  "*x+"|"
outStr = (f'{r1}\n{r2}\n'*y+r1)
print(outStr)

# The len function of a string returns an int of how many chars are in a string
# In this case, len("Aaron") would be 5

name = input("Please enter your name") # We already got the name in firstName but whatever
nameLength = len(name)
padding = f'+{"-"*nameLength}+'
print(f'{padding}\n|{name}|\n{padding}')

# Why do I find this fun?

x = 10 # Hell yeah make it real big
y = 5
r1 = f'+{"-"*nameLength}'*x+"+"
r2 = f'|{name}'*x+"|"
print(f'{r1}\n{r2}\n'*y+r1)