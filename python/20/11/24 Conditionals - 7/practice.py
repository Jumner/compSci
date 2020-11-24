from random import randint

def compare(x, y):
	if x < y:
		print(f'{x} is less than {y}')
	
	elif x > y:
		print(f'{x} is greater than {y}')

	else:
		print(f' {x} and {y} are equal')

print(compare(4, 7))

def isVowelList(c):
	vowels = ['e', 'i', 'o', 'a', 'y']
	return c in vowels

def isVowel(c):
	return c == 'e' or c == 'i' or c == 'o' or c == 'a' or c == 'y' #🤢

print(f'Character {"i"} is a vowel: {isVowel("i")}')

def determine_weightclass(weight):
	if weight > 265: return "Too heavy for weight class"
	elif weight > 205: return "Heavyweight"
	elif weight > 185: return "Light Heavyweight"
	elif weight > 170: return "Middleweight"
	elif weight > 155: return "Welterweight"
	elif weight > 145: return "Lightweight"
	else: return "Too light for weight class"

print(f'Weight {183} is in class {determine_weightclass(183)}')

print (4 < 7)
print (4 > 7)
print (True and True)
print (4 < 7 and 1 < 10)

print (True and False)
print (4 < 7 and 1 > 10)

print (True or False)
print (4 < 7 or 1 > 10)

print (not(False))

print(bool("hello"))
print(bool(""))
print(bool(100))
print(bool(0))

def is_divisible_by_3(n):
	return n % 3 == 0

print(f'{346} is divisible by 3: {is_divisible_by_3(346)}')

def calculate_payroll(hours_worked, hourly_rate):
	if hours_worked > 40:
		overtimeRate = 1.5*hourly_rate
		beforeOvertime = 40*hourly_rate
		overtime = overtimeRate * (hours_worked-40)
		return beforeOvertime + overtime
	else:
		return hourly_rate * hours_worked

print(f'Working 46 hours at a rate of $8.75 per hour pays ${calculate_payroll(46,8.75):.2f}')

def couponDiscount(price, coupon):
	taxPrice = price+price*0.13
	if coupon == "BONUS" or "BONUS40":
		return taxPrice * (1 - 0.4)
	return taxPrice

print(f'An item that costs ${239.99} costs ${couponDiscount(239.99, "BONUS40"):.2f} with coupon {"BONUS40"}')

def validDriver(age, permit, yearly_test):
	if age < 18: return permit == "G1"
	elif age <= 70: return permit == "G"
	else: return permit == "G" and yearly_test == "yes"

# I don't check yearly_test unless age > 70 so it doesn't need to be tested
# This assumes that I trust my code and i'm not sure that I do 🤨
print(validDriver(6, 'G1', 'no')) # Valid indeed
print(validDriver(16, 'G', 'no')) # False
print(validDriver(22, 'G1', 'no')) # False
print(validDriver(45, 'G', 'no')) # True
print(validDriver(77, 'G1', 'no')) # False
print(validDriver(72, 'G', 'no')) # False
print(validDriver(81, 'G1', 'yes')) # False
print(validDriver(34554, 'G', 'yes')) # True

print(f'I have my g1 and I am 16, I am a valid driver: {validDriver(16, "G1", "no")}')

# Coding bat alarm clock
def alarm_clock(day, vacation):
	if day == 0 or day == 6: # weekend

		if vacation:
			return "off"
		else:
			return "10:00"

	else:
    
		if vacation:
			return "10:00"
		else:
			return "7:00"
	# Kind of a mess but it works!

print(f'The alarm will go off at {alarm_clock(0, False)} on saturday when not on vacation')

# Coding bat Cigar party

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <= 60
	# This could also be:
	# return cigars >= 40 and (is_weekend or cigars <= 60)
	# But I thought I would keep it tidy

print(f'Party is a success on a weekday with {54} cigars: {cigar_party(54, False)}')

# Coding bat sum double

def sum_double_black_magic(a, b):
  sum = a+b
  return sum + sum*(a==b)
	# Hell yeah, booleans are numbers too!

def sum_double(a, b):
	# Now without the black magic
	sum = a+b
	if a == b: 	return 2*sum
	else: 			return sum

print(f'Sum double of {5} and {5} is {sum_double(5, 5)}')

def convert_to_day_dict(number):
	days = {
		1: "Sunday",
		2: "Monday",
		3: "Tuesday",
		4: "Wednesday",
		5: "Thursday",
		6: "Friday",
		7: "Saturday",
	} # I could also use a list and use index = number-1
		# But why would I do that when I can use a dictionary
	return days.get(number)

def convert_to_day(number):
	if number == 1: return "Sunday"
	elif number == 2: return "Monday"
	elif number == 3: return "Tuesday"
	elif number == 4: return "Wednesday"
	elif number == 5: return "Thursday"
	elif number == 6: return "Friday"
	elif number == 7: return "Saturday"

day_num = randint(1,7)
print(f'Day {day_num} is named {convert_to_day(day_num)}')

def real_root_exist(a, b, c):
	disc = b**2 - 4*a*c
	if disc > 0:
		return "Two Real Solutions"
	elif disc < 0:
		return "No Real Solutions"
	else:
		return "One Real Solution"

print("Idk how to format this its been too long since grade 10 math")
print("and unlike trig, uses for this stuff is rare")
print(f'{real_root_exist(1,2,3)}') # So i can add it later

# Take a number
def takeANumber(start, file):
	machineNumber = start
	inLine = 0
	lateStudents = 0
	for cmd in file:
		if cmd == "EOF": break # You just never know 🤪
		elif cmd == "CLOSE":
			print(lateStudents, inLine, machineNumber)
			inLine = 0
			lateStudents = 0
			# I'm sorry but this is how the gods wanted it
		elif cmd == "TAKE":
			machineNumber += 1 # PYTHON WHY!!!!!!
			inLine += 1 # WHY MUST YOU DO THIS!!!
			lateStudents += 1 # LIFE IS TORTURE!!
		elif cmd == "SERVE":
			inLine -= 1 # PLEASE MAKE IT STOP!!!!

file1 = [
"TAKE",
"TAKE",
"SERVE",
"TAKE",
"SERVE",
"SERVE",
"CLOSE",
"TAKE",
"TAKE",
"TAKE",
"SERVE",
"CLOSE",
"TAKE",
"SERVE",
"TAKE",
"SERVE",
"TAKE",
"TAKE",
"TAKE",
"TAKE",
"TAKE",
"TAKE",
"SERVE",
"CLOSE",
"EOF"] # This is kinda stupid
# And after I am done is when I realize that you gave us the code for all this
# And I refuse to use it
takeANumber(23, file1) # At least it works and it's pretty clean