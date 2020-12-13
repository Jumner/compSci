import math
# 2
# d
# r
# i
# ino
# au

# 3
wordG = "gorilla"
wordH = "hippopotamus"
wordJ = "jackal"

print(f'{wordG:>30}')
print(f'{wordH:^30}')
print(f'{wordJ:<30}')

# 4

print("aardvark" < "apple")
print("Zebra" < "anteater")
print("horse" > "cart")
print("egg" < "chicken")
# Caps are smaller "Z" < "0"

# 5

# w1 = input("Please enter word 1:  ")
# w2 = input("Please enter word 2:  ")
# if w1 > w2:
# 	print(f'Alphabetical Order: {w2} {w1}')
# else:
# 	print(f'Alphabetical Order: {w1} {w2}')

# or w1,w2 = (w2,w1)

# 6

s = "the quick brown fox jumps over the lazy dog"

print(s.count("o")) # The amount of occurrences of a string in a string
print(s.lower()) # Makes every character lowercase
print(s.replace('fox', 'lamb')) # replace all occurrences of a string with another string
print(s.find('o')) # The index of the first char of the first occurrence of a string in another string
# find also takes a start and end index

# 7

# numStr = input("Enter a number in the format 12,123:   ")
# print(f'Your number is: {numStr.replace(",", "")}')

# 8 

# word = input("Please enter a word:  ")
# word = word.title() # Makes the first letter of each word caps
# print (word)
# check = word.istitle() # Check if the first letter of each word is caps
# print (check)

# 9

def mid(word):
	# floor = math.floor((len(word)-0.5)/2) # not using // bc of consistency
	# ceil = math.ceil((len(word)+0.5)/2)
	if len(word)%2 == 0:
		floor = len(word)//2-1
		ceil = floor + 2
	else:
		floor = len(word)//2
		ceil = floor + 1

	subStr = word[floor:ceil]
	return subStr

word = "rabbit"
length = len(word)
print(mid(word))
#should print "bb"

word = "mouse"
#should print "u"
print(mid(word))

# 10

def encode_word(some_word):
	if len(some_word)%2 == 0:
		floor = len(some_word)//2-1
		ceil = floor + 2
	else:
		floor = len(some_word)//2
		ceil = floor + 1
	subStr = some_word[:floor] + some_word[ceil:] + some_word[floor:ceil]
	
	return subStr

print(encode_word("help"))
print(encode_word("thank"))

# 11

def spaced_word(some_word):
	newWord = ""
	for char in some_word:
		newWord += char + " "
	return newWord[:-1]

print(spaced_word("elephant"))
print(len(spaced_word("elephant"))) # no space after t 🤨

# 12

def print_months():
	months = "JanFebMarAprMayJunJulAugSepOctNovDec"
	for i in range(0, len(months), 3):
		month = months[i:i+3]
		print(f'{i//3+1:>2}. {month}')

print_months()

# 13

def reverse(some_string):
	newStr = ""
	for i in range(len(some_string)-1,-1,-1):
		newStr +=	some_string[i]
	return newStr

print(reverse("test"))

# 14

def count_vowels(some_string):
	e = some_string.count("e")
	i = some_string.count("i")
	o = some_string.count("o")
	a = some_string.count("a")
	y = some_string.count("y")
	u = some_string.count("u") # I fully forgot about u
	return e+i+o+a+y+u

print(count_vowels("supercalifragilisticexpialidocious"))

# 15

def remove_letter(letter, some_string):
	return some_string.replace(letter,"")

print(remove_letter('a', "apple"))