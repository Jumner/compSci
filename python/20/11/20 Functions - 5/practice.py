from math import sqrt,pi

def hypotenuse(a,b):
	c = sqrt(a**2 + b**2)
	return c

a = float(input("Enter the length of side a"))
b = float(input("Enter the length of side b"))
c = hypotenuse(a,b)

print(f'The hypotenuse of your triangle is {c:.1f}')

def convert_to_fah(c):
	f = (9/5)*c+32
	return f

celcius = float(input("Please enter temperature in Celcius"))
fahrenheit = convert_to_fah(celcius)

print(f'Temp in Celcius: {celcius:.0f}')
print(f'Temp in fahrenheit: {fahrenheit:.0f}')

def area_Circle(r):
	return pi*r**2 # Return pi*r^2
def volume_sphere(r):
	return (3/4)*(pi)*(r**3)
radius = float(input("GIVE RADIUS!!!!"))
print(area_Circle(radius))
print(volume_sphere(radius))

def is_even(num):
	return num % 2 == 0

user_num = int(input("Please enter a number"))
if is_even(user_num):
	print(f'{user_num} is even')
else:
	print(f'{user_num} is odd')

