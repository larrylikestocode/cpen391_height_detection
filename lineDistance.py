import cv2
import numpy as np
import time
# TBD
BEGINX = 0
BEGINY = 250
ENDX = 0
ENDY = 320
# ----------------- 
def readImageToRGB():
	imgBGR = cv2.imread('photos/face3.jpg')
	imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
	return imgRGB


# -----------------
# return a list of averge RGB values per line of the image 
def avgRGBLine(imgRGB):
	height = imgRGB.shape[0]
	width  = imgRGB.shape[1]

	for x in range (0, height):
		sumRGB = np.array((0,0,0))
		for y in range (BEGINY,ENDY):
			sumRGB = sumRGB + img[x][y]
		print("x value is the ", x)
		print(sumRGB//(ENDY-BEGINY))
		print("")
		time.sleep(0.5)

# -----------------
# test draw 
def testDraw(imgRGB):
























# ----------------- 
def main():


