global repeatCountry, notDone

def repeat():
	userInput = input("After surviving a country, would you like to be able to replay it? (Yes, No)\n")
	if userInput.lower() == "yes":
		return True
	elif userInput.lower() == "no":
		return False
	else:
		print("Please enter one of the options that are in brackets")
		return repeat()

def allowCountry(user, country):
	global repeatCountry, notDone
	countryNotDone = user.lower() in notDone
	if countryNotDone and not repeatCountry and user.lower() == country:
		notDone.remove(country)
	return user.lower() == country and (countryNotDone or repeatCountry)

def survive():
	global repeatCountry, notDone
	userInput = input("\nYou have survived! Great job. Would you like to quit or explore more countries? (Quit, Continue)\n")
	if userInput.lower() == "continue":
		start()
	elif userInput.lower() == "quit":
		if notDone:
			print("\nI hope that you had fun!", end="")
			if not repeatCountry:
				print(f" You had {len(notDone)} country(s) remaining\n")
			else: print()
		else:
			print("\nYou have explored all of the countries. You have won! This is the one true ending. You have survived every country. Out of all the choices you made, all of them were correct.")
	else:
		print("Please enter one of the options that are in brackets")
		survive()

def die():
	global repeatCountry, notDone
	input("\n(Press enter to continue)")
	print("\nUnfortunately, you have died. There is only one way to survive per country. ", end="")
	if not repeatCountry:
		print(f"Maybe I will add the logic to tell you that having {len(notDone)+1} country(s) remaining is good or bad.")
	else: print()

def start():
	global repeatCountry, notDone
	# notDoneTitle = list(map(lambda x: x.title(), notDone))
	notDoneTitle = []
	for country in notDone:
		notDoneTitle.append(country.title())
	notDoneStr = ", ".join(notDoneTitle)
	if notDoneStr:
		userInput = input(f"\nVacation!\nWhat Country would you like to go to? ({notDoneStr})\n")
		if allowCountry(userInput, "united states"):
			us()
		elif allowCountry(userInput, "north korea"):
			nk()
		else:
			print("Please enter one of the options that are in brackets")
			start()
	else:
		print("\nYou have explored all of the countries. You have won! This is the one true ending. You have survived every country. Out of all the choices you made, all of them were correct.")
		
def us():
	print("merica")
	survive()

def nk():
	userInput = input("\nYour baggage suspiciously never made it to Pyongyang. Do you turn around and go back or continue with the vacation?\n(Turn around, Continue)\n")
	if userInput.lower() == "turn around":
		survive()
	elif userInput.lower() == "continue":
		stay()
	else:
		print("Please enter one of the options that are in brackets")
		nk()

def stay():
	userInput = input("\nYou have decided that you will just buy any necessities in Pyongyang. Do you wander the streets or go to the hotel?\n(Streets, Hotel)\n")
	if userInput.lower() == "streets":
		streets()
	elif userInput.lower() == "hotel":
		hotel()
	else:
		print("Please enter one of the options that are in brackets")
		stay()

def streets():
	userInput = input("\nAs you walk through the streets, you develop a bit of a cough. Could it be just from the plane ride? Do you got to a doctor or just deal with it?\n(Doctor, Leave it)\n")
	# Doctor, Leave it
	if userInput.lower() == "doctor":
		doctor()
	elif userInput.lower() == "leave it":
		leaveIt()
	else:
		print("Please enter one of the options that are in brackets")
		streets()

def doctor():
	userInput = input("\nAs you get to the doctors office, per protocol, they test you for the SARS-CoV-2 virus. Unfortunately, it was not from the plane ride. You contracted Covid-19. The doctor tells you that you must go to an area to prevent the spread. You reluctantly accept.\n(Press enter to continue)")
	print("\nAs you arrive to the center, you do not see any patients. They tell you that there is only one person with covid-19 in North Korea, and they tell you that there are about to be none.")
	die()

def leaveIt():
	userInput = input("\nYou decide that you should be fine. It is only a cough from the dry air of the airplane. Over the days of your trip, your cough only worsens. Do you leave it again or go to the doctor?\n(Leave it, Doctor)\n")
	if userInput.lower() == "doctor":
		doctor()
	elif userInput.lower() == "leave it":
		leaveIt2()
	else:
		print("Please enter one of the options that are in brackets")
		leaveIt()

def leaveIt2():
	print("\nThis was no cough from the plane ride. This was Covid-19. And you weren't going to make it.")
	die()

def hotel():
	userInput = input("\nThe hotel is a little more than two kilometres away. Do you find a taxi or walk?\n(Taxi, Walk)\n")
	if userInput.lower() == "taxi":
		taxi()
	elif userInput.lower() == "walk":
		walk()
	else:
		print("Please enter one of the options that are in brackets")
		hotel()

def taxi():
	userInput = input("\nAs you leave the airport, you spot a taxi. You wave it down and give them the destination. As you arrive, the taxi driver only takes cash. However, you have just enough cash to pay them. As you arrive at the hotel, your room is on the fourth floor. There is an elevator, but it looks a bit sketchy. Do you take the stairs or the elevator?\n(Stairs, Elevator)\n")
	if userInput.lower() == "stairs":
		stairs()
	elif userInput.lower() == "elevator":
		elevator()
	else:
		print("Please enter one of the options that are in brackets")
		taxi()

# repeatCountry = repeat()
repeatCountry = False
notDone = ["united states", "north korea"]
start()