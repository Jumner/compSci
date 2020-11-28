from PIL import Image
from math import floor

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

img = Image.new('RGB', (1920, 1080), 'red')
px = img.load()
for y in range(0, img.height):
	for x in range(0, img.width):
		px[x, y] = (x%255, y%32*8, x%64*4)
		# v = floor(x/img.width*255)
		# px[x, y] = (v, v, v)
print("Done img.png")
img.save('img.png')

# img = Image.open('red.png')

newW = 240
newH = 135
dsImg = Image.new('RGB', (newW, newH))
dsImg = downSample(img, dsImg)
print("Done imgDSample.png")
dsImg.save('imgDSample.png')
dsImg = downScale(img, dsImg)
print("Done imgDScale.png")
dsImg.save('imgDScale.png')