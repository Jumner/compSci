from PIL import ImageFont, ImageDraw, Image
from random import random
# To determine the value of chars
import unicodedata

def getAsciiDict(charNum):
	font = ImageFont.truetype("/usr/share/fonts/truetype/hack/Hack-Regular.ttf")
	charWidth, charHeight = font.getsize(u"h") # Always the same
	area = charWidth * charHeight
	img = Image.new('RGB', (charWidth, charHeight))
	draw = ImageDraw.Draw(img)

	asciiDict = {}

	chars = [chr(i) for i in range(charNum) if unicodedata.category(chr(i))[0]!="C"]

	for char in chars:
		draw.text((0,0), char, font=font)
		imgPx = img.load()
		black = 0
		for y in range(img.height):
			for x in range(img.width):
				# black += imgPx[x,y] == (0,0,0)
				black += imgPx[x,y][0]/255
				imgPx[x,y] = (0,0,0)
		value = 255*black/area
		asciiDict[value] = char
	
	# Post processing
	finalDict = {}
	maxV = max(asciiDict)
	SF = 255/max(asciiDict)
	for key in asciiDict:
		finalDict[key*SF] = asciiDict[key]
	return finalDict

font = ImageFont.truetype("/usr/share/fonts/truetype/hack/Hack-Regular.ttf")
charWidth, charHeight = font.getsize(u"h") # Always the same
area = charWidth * charHeight
img = Image.new('RGB', (charWidth, charHeight))
draw = ImageDraw.Draw(img)

asciiDict = {}

chars = [chr(i) for i in range(2048)]

for char in chars:
	draw.text((0,0), char, font=font)
	imgPx = img.load()
	black = 0
	for y in range(img.height):
		for x in range(img.width):
			black += imgPx[x,y] == (0,0,0)
			imgPx[x,y] = (0,0,0)
	value = 255*(area-black)/area
	asciiDict.update({value:char})