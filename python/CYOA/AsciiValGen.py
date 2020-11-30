from PIL import ImageFont, ImageDraw, Image
# To determine the value of chars
from collections import OrderedDict
from bisect import bisect_left
import unicodedata

def getAsciiDict(charNum):
	font = ImageFont.truetype("/usr/share/fonts/truetype/hack/Hack-Regular.ttf")
	charWidth, charHeight = font.getsize(" ") # Always the same
	area = charWidth * charHeight # area of the font
	img = Image.new('RGB', (charWidth, charHeight))
	draw = ImageDraw.Draw(img)

	asciiDict = OrderedDict()

	chars = [chr(i) for i in range(charNum) if unicodedata.category(chr(i))[0]!="C"] # Get every drawable char

	for char in chars:
		draw.text((0,0), char, font=font) # Draw char to screen
		imgPx = img.load()
		bright = 0 # value of the char
		for y in range(img.height):
			for x in range(img.width): # every pixel of the char
				bright += imgPx[x,y][0]/255 # Add value of pixel to value of char
				imgPx[x,y] = (0,0,0) # Make pixel black bc we never reset it
		value = bright/area # sum of char pixel values over max value
		asciiDict[value] = char # Store it away
	
	# Post processing
	finalDict = {}
	SF = 255/max(asciiDict)
	# What the largest value has to be * by to be 255
	for key in sorted(asciiDict): # sort it for binary search
		finalDict[key*SF] = asciiDict[key] # Multiply keys to be from hopefully 0-255
		# It's fine if these are off as it grabs the closest one to the value of the pixel
	return finalDict

def getAnsiDict():
	ansiDict = {
		0:'\033[31;1;40m',
		42.5:'\033[33;1;40m',
		85:'\033[32;1;40m',
		127.5:'\033[36;1;40m',
		170:'\033[34;1;40m',
		212.5:'\033[35;1;40m',
		255:'\033[31;1;40m'
	} # I just don't want to see it tbh 🙃
	return ansiDict

def closest(dict, key, keyList=-1):
	if keyList == -1: # Grab the keylist if it was not passed
		# This would be done per pixel so pass it if possible
		keyList = list(dict.keys())

	keyIndex = bisect_left(keyList, key) # Do the searching
	
	try:
		hKey = keyList[keyIndex]
	except IndexError as err: # "list index out of range" 😒
		print(f'hKey: {err}') # Just so we know
		hKey = 0
	try:
		lKey = keyList[keyIndex-1]
	except IndexError as err: # "list index out of range" 😒
		print(f'lKey: {err}') # Just so we know
		lKey = 0

	if abs(hKey-key) > abs(lKey-key): # Which one is closer to the key
		return dict[hKey]
	else:
		return dict[lKey]