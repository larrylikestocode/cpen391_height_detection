import cv2
import numpy as np

BEGINX = 0
BEGINY = 0
ENDX = 0
ENDY = 0
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

	# for x in range () 


# -----------------
# test draw 
def testDraw(imgRGB):
	























# ----------------- 
def main():


