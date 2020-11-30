from PIL import Image
from math import floor
from random import randint, random
from collections import OrderedDict
from bisect import bisect_left

from AsciiValGen import getAsciiDict, getAnsiDict, closest
from ds import downScale

def printHsv(hsvImg, ansiDict, asciiDict):
	hsvImgPx = hsvImg.load()
	reset = '\033[37;49m' # Console reset escape sequence
	pStr = "" # Start it with a reset char
	
	asciiKeys = list(asciiDict.keys())
	ansiKeys = list(ansiDict.keys())

	for y in range(hsvImg.height):
		if pStr: # Only reset and \n after a line
			pStr += reset + '\n'
		for x in range(hsvImg.width):
			if hsvImgPx[x,y][1] < 50: # If pixel is unsaturated
				ansiSeq = '\033[37;1;40m' # White
			else: # Pixel is saturated
				hue = hsvImgPx[x,y][0] * (0.9+random()*0.1) # Make it a bit random
				ansiSeq = closest(ansiDict, hue, ansiKeys) # Grab the closest color to the hue
			pStr += ansiSeq

			value = hsvImgPx[x,y][2] * (0.9+random()*0.1) # Make it a bit random so its not uniform
			char = closest(asciiDict, value, asciiKeys) # Grab the closest char to brightness value
			pStr += char
	file = open("str.txt", 'w')
	file.write(pStr+reset) # Put it into a file for copy pasting
	file.close()
	print(pStr+reset)

def printImg(img, width=196, charNum=2048):
	asciiDict = getAsciiDict(charNum) # Grab the dictionaries
	ansiDict = getAnsiDict()

	dsImg = downScale(img, width) # Downscale to image
	
	hsvImg = dsImg.convert('HSV')
	
	printHsv(hsvImg, ansiDict, asciiDict) # Print it!

# img = Image.new('RGB', (1920, 1080), 'red')
# px = img.load()
# for y in range(0, img.height):
# 	for x in range(0, img.width):
# 		px[x, y] = (2*(x%128), x%256, floor(0.5*(x%512)))
# img.save('img.png')

img = Image.open('1kx100x3.png') # 1kx100x3.png sunrise.jpeg img.png
print("Img opened")

printImg(img)