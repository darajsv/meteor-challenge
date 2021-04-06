from PIL import Image
from numpy import asarray

countMeteors = 0
countStars = 0
xcoord = 0
ycoord = 0
redCoordinates = []
blueCoordinates = []


ogImage = Image.open("meteor_challenge_01.png")  # opens image
pixelsArray = asarray(ogImage)  # transforms image in array

print(ogImage)  # data about image

for matrix in pixelsArray:  # in each position of pixel array there is a matrix
    # each line of the matrix is a pixel in RGBA [r , g, b , a]
    for pixel in matrix:
        if(pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 0):  # finds red pixels (meteors)
            countMeteors = countMeteors + 1
            redCoordinates.append([xcoord, ycoord])
        if(pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255):  # finds white pixels (stars)
            countStars = countStars + 1
        if(pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 255):  # finds blue pixels (water)
            if(ycoord == 512):  # only append coordinates whom y is 512 (top part of the water)
                blueCoordinates.append([xcoord, ycoord])
        xcoord = xcoord+1
    ycoord = ycoord+1
    xcoord = 0

meteorHitsWater = 0
for redPixel in redCoordinates:
    for bluePixel in blueCoordinates:
        # if the xCoord of a meteor is equal to a xCoord of the water then the meteor will hit the water
        if redPixel[0] == bluePixel[0]:
            meteorHitsWater = meteorHitsWater + 1

print("-------------------------------------------------------")
print("Number of Stars | ", countStars)
print("Number of Meteors | ", countMeteors)
print("Meteors falling on the Water | ", meteorHitsWater)
print("-------------------------------------------------------")
