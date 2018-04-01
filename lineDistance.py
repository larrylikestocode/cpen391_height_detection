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
	avglist[];

	for x in range (0, height):
		sumRGB = np.array((0,0,0))
		for y in range (BEGINY,ENDY):
			sumRGB = sumRGB + imgRGB[x][y]
		avglist.append(sumRGB//(ENDY-BEGINY))

		print("x value is the ", x)
		print(avglist[0])
		print(avglist[1])
		print("")
		time.sleep(0.5)



# ----------------- 
def main():
        img = readImageToRGB()
        avgRGBLine(img)
main()






# -----------------
# test draw 
def testDraw(imgRGB):
        black = np.array((0,0,0))
        for x in range(260,270):
                for y in range(650,1200):
                        imgRGB[x][y] = black
                        
                print(imgRGB[x][y])
        imgBGR = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)         
        cv2.imwrite("photos/color_black.jpg",imgBGR)
