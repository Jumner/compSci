name = input("Enter your name")
print(f'{name} here, this is my first program\n\n')
# Newline char to create space after the print statement
print(f'Hello {name}')
print("Hello World")
# print(Hello World) # Gets error "SyntaxError: invalid syntax"
print(1,000,000)  # Prints 1 0 0
# print(1 2) # Gets error "SyntaxError: invalid syntax"
# print(n = 7) # Gets error "TypeError: 'n' is an invalid keyword argument for print()"
print(7+5)
print(f'5 is less than {7-1} which is less than 7')
print(5, "is less that", 7-1, "which is less than", 7)
print("\n\n")
pi = 62.83185 / (2*10)
print(f'The value of pi to 5 decimal places approximately {pi:.4f}')
print(f'10/3 = {10/3:>10.2f}')
name = 'Avery'
print(f'--{name:^10}--')

print(6 * (1 - 2 + 3))
print(6 * 1 - (2 + 3))
print(6 * (1 - 2) + 3)

print(10/3)  # The decimal result of 10 divided by 3
print(10//3)  # The result of 10/3 floored
print(10 % 3)  # The remainder after 10/3
# You can use // to get the floor and % to get the remainder

# Lesson 1 Homework
# # 01234 segment number
# 1 00100 
# 2 10111 
# 3 10110 
# 4 01110 
# 5 11010 
# 6 11011 
# 7 10100 
# 8 11111 
# 9 11110 
# 0 11101 

# Conclusion two can safely be removed
# Brute force method
# Each number can be represented as a byte which stores if each of the seven segments are on or off
# then starting at the first bit, set the first bit of every bite to 0 check if any of them are the same
# if two are the same, add one to a counter char and revert that bit. and move to the next bit