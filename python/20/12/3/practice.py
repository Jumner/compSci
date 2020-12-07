from time import sleep
from math import ceil
# Example 1
# 0
# 10
# 20
# 30
# 40

# Example 2
# 1. "Hello World!"
# ..
# 20. "Hello World!"

# Example 3
# 0 - 0: The Matrix
# ..
# 0 - 4: The Matrix
# ..
# 9 - 4: The Matrix

# Example 4
# 10
# 18
# 24
# 28
# 30
# 30
# 28
# 24
# 18
# 10

# Example 5
# 604800

# 2

for i in range(5,1000,5):
    # print(i)
		pass

# 3

def print_times_table(table_number):
	for i in range(1, 11):
		print(f'{i:2} x {table_number} = {i*table_number:4}')

print_times_table(9)

# 4

def print_temperature_table():
	print("Celcius to Fahrenheit Table")
	print('-'*27)
	for c in range(-20, 36, 5):
		f = c * 9/5 + 32
		print(f'{c:>3} C --> {f:>3.0f} F')

print_temperature_table()

# 5

total = 0
for num in range(1,101):
	total += num
print(total)

# 6

def sum_range_values(low,high):
	sum = 0
	for i in range(low,high+1):
		sum += i
	return sum

lowEnd = eval(input("Enter the low end of range"))
highEnd = eval(input("Enter the high end of range"))
print(sum_range_values(lowEnd, highEnd))

# 7

rangeStr = ""
for i in range(highEnd, lowEnd-1, -1):
	rangeStr += f'{i}, '
print(rangeStr)

# 8

for i in range(10, 0, -1):
	print(f'{i} ...')
	# sleep(0.5)

# 9

def sum_squares(some_num):
	numSum = 0
	for i in range(some_num):
		numSum += (i+1)**2
	return numSum

print(sum_squares(5))

# 10

triStr = ""
for i in range(10):
	triStr += "$"*(i+1) + "\n"

for i in range(10, 0, -1):
	triStr += "$"*(i) + "\n"

for i in range(10):
	triStr += f'{"$"*(i+1):>10}' + "\n"

for i in range(10, 0, -1):
	triStr += f'{"$"*(i):>10}' + "\n"

print(triStr)

patStr = ""

# 11

n = 15
w = n*2-2
for i in range(n):
	print(f'{i+1:>{i+1}}{" ":^{(w+3)-i*2}}{i+1}')

num = eval(input("Enter a number"))

h = ceil((num)/2) # Why add 1 when we can round up?
for i in range(h):
	print(f'{"*"+2*i*"*":^{num}}')