'''
Python Part II
Homework submission 1

created by you
'''
import random



#Question 4
#Write a function that uses a for loop to generate a Celcius to Fahrenheit table.

def print_temperature_table():
	print("Celcius to Fahrenheit Table")
	print('-'*27)
	for c in range(-20, 35+1, 5):
		f = c * 9/5 + 32
		print(f'{c:>4} C --> {f:>4.0f} F')

#MAIN
print_temperature_table()



#Question 9
#Write a function that sums the squares from 1 ... n inclusive.

def sum_squares(some_num):
	total = 0
	for i in range(1,some_num+1):
		total += i**2
	return total

def sum_squares_clean(some_num):
    squaresList = [i**2 for i in range(1,some_num+1)]
    # squaresList = [(i+1)**2 for i in range(some_num)] # I this one better in your opinion?
    return sum(squaresList) 

#MAIN
n = random.randint(5, 25)
#don't forget to call the function and print the result ...
print(f'The sum of the squares of all the numbers from 1 to {n} is {sum_squares(n)}')