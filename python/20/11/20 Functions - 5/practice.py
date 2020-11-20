from math import sqrt,pi

def hypotenuse(a,b):
	c = sqrt(a**2 + b**2)
	return c # I really don't find this any easier to read tbh

a = float(input("Enter the length of side a"))
b = float(input("Enter the length of side b"))
c = hypotenuse(a,b)

print(f'The hypotenuse of your triangle is {c:.1f}')

def convert_to_fah(c):
	f = (9/5)*c+32
	print(f'Temp in Celcius: {c:.0f}')
	print(f'Temp in fahrenheit: {f:.0f}')
	return f # Return this in case the user wants it

celcius = float(input("Please enter temperature in Celcius"))
fahrenheit = convert_to_fah(celcius) # Store it incase we need it later

def area_Circle(r):
	return pi*r**2 # Return pi*r^2
def volume_sphere(r):
	return (3/4)*(pi)*(r**3)

radius = float(input("GIVE RADIUS!!!!"))
print(f'Area of circle with radius {radius}: {area_Circle(radius)}')
print(f'Volume of sphere with radius {radius}: {volume_sphere(radius)}')

def is_even(num):
	return num % 2 == 0

user_num = int(input("Please enter a number"))
if is_even(user_num):
	print(f'{user_num} is even')
else:
	print(f'{user_num} is odd')

def calculate_tax(price):
	return price*0.13
user_price = 109.99

print(f'Wow this costed {user_price}$ with {calculate_tax(user_price)}$ of tax')

def formatName(name):
	s = '*'*(len(name)+2) + '\n'
	s += f'*{name}*\n'
	s += '*'*(len(name)+2) + '\n'
	return s

print(formatName("Justin"))

def clear_screen():
	print("\n"*25)

clear_screen()

def is_leap_year(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2000)) # True
print(is_leap_year(2004)) # True
print(is_leap_year(2100)) # False