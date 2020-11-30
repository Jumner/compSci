from PIL import Image
from math import floor
# Either down sample or down scale

def downSample(img, dsImg):
	# Take an input image and an image to down sample
	imgSF = [1/img.width, 1/img.height] # Grab the scale factors
	dsImgSF = [1/dsImg.width, 1/dsImg.height]
	SF = [d / f for d, f in zip(dsImgSF, imgSF)] # Total scale factor
	imgPx = img.load()
	dsImgPx = dsImg.load()
	for y in range(0, dsImg.height):
		for x in range(0, dsImg.width):
			imgX = floor(x * SF[0]) # Grab corresponding pixel
			imgY = floor(y * SF[1])
			dsImgPx[x,y] = imgPx[imgX, imgY]
	return dsImg

def downScale(img, width):
	# Take an input image and an image to down scale
	aspectRatio = img.height / img.width # ar of original image
	height = round(aspectRatio*width/2) # new height at half aspect ratio bc chars are tall
	dsImg = Image.new('RGB', (width, height))

	imgSF = [1/img.width, 1/img.height] # Grab the scale factors
	dsImgSF = [1/dsImg.width, 1/dsImg.height]
	SF = [d / f for d, f in zip(dsImgSF, imgSF)] # Total scale factor
	imgPx = img.load()
	dsImgPx = dsImg.load()
	for x in range(0, dsImg.width):
		for y in range(0, dsImg.height):
			lx = floor(x * SF[0]) # Get the boundary indices
			ux = floor((x+1) * SF[0])
			ly = floor(y * SF[1])
			uy = floor((y+1) * SF[1])
			col = (0,0,0) # Set starting col
			for ix in range(lx, ux):
				for iy in range(ly, uy): # Every corresponding pix in the full img
					col = tuple(map(lambda c,i: c + i, col, imgPx[ix, iy])) # Add col and the img color
			col = tuple(map(lambda c: floor(c/((ux-lx)*(uy-ly))), col)) # divide by size of block
			dsImgPx[x,y] = col
	return dsImg