from datetime import datetime as d

def calculate_age(year_of_birth):
	return d.now().year - year_of_birth


birth_year = int(input("Enter the year you were born"))
print(f'You will turn {calculate_age(birth_year)} in {d.now().year}')

