from PIL import Image
from math import floor
from random import randint
from AsciiValGen import getAsciiDict

def downSample(img, dsImg):
	# Take an input image and an image to down sample
	imgSF = [1/img.width, 1/img.height]
	dsImgSF = [1/dsImg.width, 1/dsImg.height]
	SF = [d / f for d, f in zip(dsImgSF, imgSF)]
	imgPx = img.load()
	dsImgPx = dsImg.load()
	for y in range(0, dsImg.height):
		for x in range(0, dsImg.width):
			imgX = floor(x * SF[0])
			imgY = floor(y * SF[1])
			dsImgPx[x,y] = imgPx[imgX, imgY]
	return dsImg

def downScale(img, dsImg):
	# Take an input image and an image to down scale
	imgSF = [1/img.width, 1/img.height]
	dsImgSF = [1/dsImg.width, 1/dsImg.height]
	SF = [d / f for d, f in zip(dsImgSF, imgSF)]
	imgPx = img.load()
	dsImgPx = dsImg.load()
	for x in range(0, dsImg.width):
		for y in range(0, dsImg.height):
			lx = floor(x * SF[0])
			ux = floor((x+1) * SF[0])
			ly = floor(y * SF[1])
			uy = floor((y+1) * SF[1])
			col = (0,0,0)
			for ix in range(lx, ux):
				for iy in range(ly, uy):
					col = tuple(map(lambda c,i: c + i, col, imgPx[ix, iy]))
			col = tuple(map(lambda c: floor(c/((ux-lx)*(uy-ly))), col))
			dsImgPx[x,y] = col
	return dsImg

def saveHsv(hsvImg, file):
	hsvImg.convert('RGB').save(file)

def printHsv(hsvImg, ansiTable, asciiDict):
	hsvImgPx = hsvImg.load()
	reset = '\033[37;49m'
	pStr = reset
	for y in range(hsvImg.height):
		pStr += reset + '\n'
		for x in range(hsvImg.width):
			if hsvImgPx[x,y][1] < 50:
				ansiChar = '\033[37;1;40m'
			else:
				hue = hsvImgPx[x,y][0]
				ansiChar = ansiTable.get(hue) or ansiTable[min(ansiTable.keys(), key = lambda key: abs(key-hue))]
			pStr += ansiChar

			value = hsvImgPx[x,y][2]
			char = asciiDict.get(value) or asciiDict[min(asciiDict.keys(), key = lambda key: abs(key-value))]
			pStr += char
	file = open("str.txt", 'w')
	file.write(pStr+reset)
	file.close()
	print(pStr+reset)

img = Image.new('RGB', (1920, 1080), 'red')
px = img.load()
for y in range(0, img.height):
	for x in range(0, img.width):
		px[x, y] = (x%255, y%64*4, x%128*2)
img.save('img.png')

img = Image.open('1kx100x3.png')
ar = img.height/img.width

newW = 64
newH = round(ar*newW/2)
print(newH) # 18 / 36
dsImg = Image.new('RGB', (newW, newH))
dsImg = downScale(img, dsImg)
dsImg.save('imgDScale.png')

hsvImg = dsImg.convert('HSV')

g = '\033[32;40m'
r = '\033[37;49m'

ansiTable = {
	0:'\033[31;1;40m',
	255:'\033[31;1;40m',
	120:'\033[32;1;40m',
	60:'\033[33;1;40m',
	240:'\033[34;1;40m',
	300:'\033[35;1;40m',
	180:'\033[36;1;40m',
}

asciiDict = getAsciiDict(1024)
printHsv(hsvImg, ansiTable, asciiDict)


print(min(asciiDict))
print(max(asciiDict))

saveHsv(hsvImg, 'hsvImg.png')