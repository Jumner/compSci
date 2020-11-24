from math import pi # Used to get circle area and sphere volume

#Question 3

def area_Circle(r):
	return pi*r**2 # Return pi*r^2

def volume_sphere(r):
	return (3/4)*(pi)*(r**3)

#Your main for question 3

# radius = float(input("Enter the radius: "))
radius = 4

area = area_Circle(radius)
volume = volume_sphere(radius)
print(f'The area of circle with radius {radius} is {area:.10f}') # I know how to do formatting lol
print(f'The volume of sphere with radius {radius} is {volume:.10f}')

#Question 5

def calculate_tax(price):
	return price*0.13

#Your main for question 5

# user_price = float(input("What did the item cost before tax?: "))
user_price = 109.99

tax = calculate_tax(user_price)
print(f'This item costed ${user_price:.2f} before tax with ${tax:.2f} of tax')
print(f'This means that the item costed ${(user_price+tax):.2f} including tax')