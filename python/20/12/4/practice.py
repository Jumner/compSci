from random import randint
# 1
continue_repeat = "end"
continue_repeat = "please no"

while continue_repeat == "end":
  print("Have a good day")

# 2-3
user_input = "more"
count = 0

while user_input == "more":
	count += 1
	print ("Have a good day.")
	user_input = input("Type more to continue")
     
print (f'Done, looped {count} times')

# 4
total_sum = 0
number_of_numbers = 0
while user_input != 0:
	user_input = eval(input("Enter a number to be added, enter 0 to stop"))
	total_sum += user_input
	number_of_numbers = number_of_numbers+1 if user_input != 0 else number_of_numbers
	print(f'Entered {user_input} for a sum of {total_sum} and an average of {total_sum/number_of_numbers}')

# 5
count = 0
stock = 25.23
while stock < 100:
	stock*=1.163
	count += 1
	print(f'Stock costs ${stock:.2f} after {count} years')
print(f'Stock surpassed $100 after {count} years')

# 6
for i in range(20):
	print(f'{i+1:>3} X 5 = {(i+1)*5}')

# 7
total = 0
count = 0
while total < 100:
	count += 1
	roll = randint(1,6)
	total += roll
	print(f'Rolled a {roll} >>> total is {total}')
print('-'*20)
print(f'Total number  of rolls {count}')

# 8
total = 0
count = 0
while total < 100:
	count += 2
	roll = randint(1,6)
	total += roll
	print(f'Die 1 rolled a {roll} >>> total is {total}')
	roll = randint(1,6)
	total += roll
	print(f'Die 2 rolled a {roll} >>> total is {total}')
print('-'*20)
print(f'Total number  of rolls {count}')

# 9
count = 0
initRoll = randint(1,6)
roll = 0
print(f'Your first roll is {initRoll}')
while roll != initRoll:
	count += 1
	roll = randint(1,6)
	print(f'Rolled a {roll}')
print('-'*20)
print(f'It took {count} rolls to reach your point of {initRoll} again')

# 10
rNum = randint(1,10)
guess = 0
print("I have picked a random number between 1 and 10. What is it?")
while guess != rNum:
	guess = eval(input("Guess the random number"))
	if guess > rNum:
		print(f'{guess} is too high')
	elif guess < rNum:
		print(f'{guess} is too low')
	else:
		print(f'{guess} is correct! Well done!')
	
# 11
nums = [randint(1,50) for i in range(2)]
guess = 0
while guess != sum(nums):
	guess = eval(input(f'{nums[0]:>3} +{nums[1]:>3} = ???'))
	if guess != sum(nums):
		print("Sorry that is incorrect. Try again")
	else:
		print(f'You got it right! {nums[0]:>3} +{nums[1]:>3} ={sum(nums):>3}')

# 12 oh yeah im extra

def word_in_word(guess, word):
	for letter in guess:
		if letter not in word.lower():
			return False
	return True

point = 0
word = "happenings"
guess = word
correct = []

while True:
	guess = input("Enter a word you find in happenings")
	if word_in_word(guess, word):
		if guess in correct:
			print(f"You already guessed {guess}. Try again")
			continue
		point += len(guess)
		correct.append(guess)
		print(f'Congratulations you found a word. Score {point}')
	else:
		break

print(f"Sorry {guess} doesn't exist in {word}\nFinal score {point}")