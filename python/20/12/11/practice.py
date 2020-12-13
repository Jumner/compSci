# Lists are mutable
# string = string.lower()
# list.append()
import random

# 1

list_numbers = [5, 6, 3, 2, 54, 32, 23, 12, 21, 75, 43, 1]
min_in_list = min(list_numbers)
print(min_in_list)

wordList = ["Zebra", "apple", "asfdgsdg"]
min_wordList = min(wordList)
print(min_wordList)

# 3

def make_random_list(quantity):
	random_numbers = []
	for i in range(quantity):
		random_numbers.append(random.randint(0,99))
	return random_numbers

result = make_random_list(50)
print(max(result))

# 3

def make_random_list(quantity):
	random_numbers = []
	for i in range(quantity):
		random_numbers.insert(0, random.randint(0,99))
	return random_numbers

result = make_random_list(50)
print(max(result))

# 4

def someListFunction(a, i):
   temp = a[i]
   for j in range( i, len(a) - 1): # Iterate through from i to end
      a[j] = a[j + 1] # Set everything starting at i to the one above
			# This would overwrite a[i] which is why it's stored

   del a[len(a) - 1] # Remove the duplicate end

   return temp # Return item at index
# looks like pop to me chief

# 5

def list_average(some_list):
	avg = sum(some_list)/len(some_list)
	return avg
print(list_average([i for i in range(10)]))

# 6

people = ['Rema Wilkin', 'Kiyoko Sandor', 'Heriberto Cruikshank', 'Demetria Novoa', 'Clelia Necessary', 'Mahalia Spadaro', 'Barry Ager', 'Collin Blanche', 'Pearline Sokoloff', 'Garland Hedgecock', 'Nicola Deltoro', 'Shaniqua Mendelson', 'Kris Bucy', 'Rashida Koester', 'Elane Sweetser', 'Estela Lawley', 'Micki Brass', 'Emmanuel Tufts', 'Lenita Michalec', 'Ha Mcelhannon', 'Domonique Sutera', 'Hoyt Camden', 'Arlyne Messenger', 'Dagmar Berra', 'Gregoria Belmont', 'Sylvie Guyette', 'Gaston Christianson', 'Lora Holleman', 'Lesley Leininger', 'Paige Nolen']

print(f'{"Lastname,":<15} {"Firstname":<15}')
print("-"*31)

for name in people:
	nameList = name.split()
	print(f"{nameList[1]:<15} {nameList[0]:<15}")

# 7

def list_greater_smaller(some_list):
	count_greater50 = 0
	count_less50 = 0
	for num in some_list:
		# count_less50 += num<50 # It's I love treating bools like numbers
		# count_greater50 += num>50 # It may not be intuitive but it's so satisfying 🙂
		if num > 50:
			count_greater50 += 1
		elif num < 50:
			count_less50 += 1

	return (count_greater50, count_less50)


#MAIN
your_random_list = make_random_list(50)
more_than50, less_than50 = list_greater_smaller(your_random_list)
print(more_than50, less_than50)

# 8

cities = ['Badalona', 'Calama', 'Dadu', 'Enshi', 'Kano', 'Haldia', 'Passos']

#example 1
for city in cities:
	print(f'{city:<12} and variable city is datatype {type(city)}')

print("\n\n")

#example 2
for index in range(0, len(cities)):
	print(f'{index:<2} {cities[index]:<12} and variable index is datatype {type(index)}')

# I like using i but you will never catch me lacking and using i for anything but an index 🤣

# 9

userInput = ""
userList = []
while userInput != "end":
	# userInput = input("Please enter an item to add to list type 'end' to complete: ")
	userInput = "end"
	userList.append(userInput)
userList.remove("end")

userList.sort()
print(f'Your list is {userList}')

# 10

def getMonthName(monthNum):
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	return months[monthNum-1]

# m = int(input("Please enter the month number"))
m = 6
print(getMonthName(m))

# 11

zoo_1 = ['bengal tiger', 'caspian tiger', 'indochinese tiger', 'lion', 'jaguar', 'cougar', 'leopard', 'snow leopard', 'cheetah', 'clouded leopard']
zoo_2 = ['siberean tiger', 'south china tiger', 'lion', 'snow leopard', 'clouded leopard']

# unique_species = [species for species in zoo_1 if species in zoo_2]
unique_species = [] # Common species? "to create a list of similar items, items that exist in both lists"
for species in zoo_1:
	if species in zoo_2:
		unique_species.append(species)
print("The two zoos each have these species")
print("-"*40)
for species in unique_species:
	print(species)

# 12

# import random

def generate_characters(quantity):
    
	lastnames = ['Wilson', 
'Peralta', 
'McCaffrey', 
'Betts', 
'Willis', 
'Ewing', 
'Franklin', 
'Carey', 
'Parra', 
'Walters', 
'Beck', 
'Cole', 
'Armstrong', 
'Stone', 
'Henderson', 
'Harrison', 
'Dixon', 
'Brady', 
'Jimenez', 'Fitzgerald']
	firstnames = ['Todd', 
'Nicholas', 
'Teresa', 
'Jennifer', 
'Gloria', 
'Bobby', 
'Angela', 
'Justin', 
'Kimberly', 
'Arthur', 
'John', 
'Johnny', 
'Carol', 
'Brian', 
'Heather', 
'Jason', 
'Daniel', 
'Norma', 
'Eric', 
'Douglas', 
'Paula', 
'Larry', 
'Eugene', 
'Ruth', 'Betty']
	cities = ['Fez', 'Budapest', 'Rome', 'Hong Kong', 'Mexico City', 'Milan', 'Philadelphia', 'Dallas', 'Sana\'a']
	occupation = ['Architect', 'Librarian', 'Illustrator', 'Landscape gardner', 'Bank clerk', 'Au pair', 'Legal secretary', 'Property developer', 'Publisher']

	characters = []

	for i in range(0, quantity):
		lastName = random.choice(lastnames)
		firstName = random.choice(firstnames)
		age = random.randint(18,50)
		city = random.choice(cities)
		job = random.choice(occupation)

		character = f"{lastName}, {firstName}, {age}, {city}, {job}"

		characters.append(character)



        


	return characters

def print_characters(aList):

	print("Characters in list are")
	print("-"*30)
	for i in range(0, len(aList)):
		print(f'{i+1:>3}. {aList[i]}')
        

#main
number_characters = int(input("How many random characters do you wish to generate?"))

list_characters = generate_characters(number_characters)

print_characters(list_characters)

    
