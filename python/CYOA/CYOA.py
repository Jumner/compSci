def start():
	funcDict = {
		"north america": "na()",
		"asia": "asia()"
	}
	user = input("\nYou are going on vacation!\nWhat continent would you like to travel to?\n(North America, South America, Europe, Asia, Africa, Australia)\n")
	if user.lower() in funcDict: # if input is a key in the dict
		eval(funcDict[user.lower()]) # run the content at the users key
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		start() # recurse if input is not a key in the dict

def na():
	funcDict = {
		"mexico": "mex()",
		"united states": "us()"
	}
	user = input("\nYou chose to go to North America.\nWhat country in North America would you like to travel to?\n(Mexico, United States)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		start()

def asia():
	funcDict = {
		"north korea": "nk()",
		"china": "china()"
	}
	user = input("\nYou chose to go to Asia.\nWhat country in Asia would you like to travel to?\n(North Korea, China)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		asia()

def nk():
	funcDict = {
		"turn around": "turnAround()",
		"continue": "cont()"
	}
	user = input("\nYour baggage suspiciously never made it to Pyongyang.\nWhat do you do?\n(Turn around, Continue)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		nk()

def turnAround():
	funcDict = {
		"yes": "start()",
		"no": "print(\"Thank you for playing :)\")"
	}
	user = input("\nCongratulations, you have survived North Korea!\nWould you like to travel to a different country?\n(Yes, No)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		turnAround()

def cont():
	funcDict = {
		"streets": "streets()",
		"hotel": "hotel()"
	}
	user = input("\nYou have decided that you will just buy any necessities in Pyongyang.\nWhat do you do first?\nExplore the streets or go to the hotel (Streets, Hotel)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		cont()

def streets():
	funcDict = {
		"leave it": "leaveIt()",
		"doctor": "doctor()"
	}
	user = input("\nAs you walk through the streets, you develop a bit of a cough. Could it be just from the plane ride?\n Do you go to a doctor or just deal with it?\n(leave it, doctor)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		streets()

def leaveIt():
	funcDict = {
		"leave it": "leaveIt2()",
		"doctor": "doctor()"
	}
	user = input("\nYou decide that you should be fine. It is only a cough from the dry air of the airplane. Over the days of your trip, your cough only worsens.\nDo you leave it again or go to the doctor?\n(leave it, doctor)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		leaveIt()

def leaveIt2():
	print("\nThis was no cough from the plane ride. This was Covid-19. And you weren't going to make it.\n")

def doctor():
	funcDict = {
		"yes": "noPatients()"
	}
	user = input("\nAs you get to the doctors office, per protocol, they test you for the SARS-CoV-2 virus. Unfortunately, it was not from the plane ride. You contracted Covid-19. The doctor tells you that you must go to an area to prevent the spread.\nDo you accept?\n(yes)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		doctor()

def noPatients():
	print("\nAs you arrive to the center, you do not see any patients. They tell you that there is only one person with Covid-19 in North Korea, and they tell you that there are about to be none.\n")

def hotel():
	funcDict = {
		"taxi": "taxi()",
		"walk": "walk()"
	}
	user = input("\nThe hotel is a little more than two kilometres away.\nDo you find a taxi or walk?\n(taxi, walk)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		hotel()

def taxi():
	funcDict = {
		"stairs": "stairs()",
		"elevator": "elevator()"
	}
	user = input("\nAs you leave the airport, you spot a taxi. You wave it down and give them the destination. As you arrive, at the hotel, your room is on the fourth floor. There is an elevator, but it looks a bit sketchy.\nDo you take the stairs or the elevator (stairs, elevator)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		taxi()

def stairs():
	funcDict = {
		"talk": "talk()",
		"flee": "flee()"
	}
	user = input("\nIt is tiring to carry your bags up the stairs but it better than the sketchy elevator right? As you get to your room, there are people in uniforms waiting there for you. Maybe you said too much on the plane ride.\nDo you try to talk to them or try to flee (talk, flee)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		stairs()

def talk():
	print("\nAs you approach them, they start walking towards you. They take you away and you live the rest of your life in a work camp.\n")

def flee():
	print("\nYou try to run, but it is hopeless. You are surrounded. They capture you and send you to a work camp where you spend the rest of your life.\n")

def elevator():
	print("\nAs the elevator travels upwards, it seems to stop. However, you are not at the fourth floor. You are not at any floor. You yell for help but it is hopeless. Nobody comes to rescue you.\n")	

def walk():
	funcDict = {
		"yes": "elevator2()"
	}
	user = input("\nYou finally make it to the hotel. Your room is on the fourth floor. Once you check in and get your room key, you are too tired to take the stairs.\nDo you take the elevator?\n(yes)\n")
	if user.lower() in funcDict:
		eval(funcDict[user.lower()])
	else:
		print("\nPlease enter one of the values that are in parentheses.")
		walk()

def elevator2():
	print("\nAs the elevator travels upwards, it seems to stop. However, you are not at the fourth floor. You are not at any floor. You are too tired to yell for help and shortly collapse from exhaustion.\n")

start()