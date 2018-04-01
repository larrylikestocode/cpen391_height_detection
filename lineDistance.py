import cv2
import numpy as np
import time
import math 
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
	avglist=[];

	for x in range (0, height):
		sumRGB = np.array((0,0,0))
		for y in range (BEGINY,ENDY):
			sumRGB = sumRGB + imgRGB[x][y]
		avglist.append(sumRGB//(ENDY-BEGINY))
	return avglist	

# ----------------
# take an RGB value and then return the percentage diff
def calculatediffHelper(colorRGB1, colorRGB2):
    r = (colorRGB1[0] + colorRGB2[0])/2
    deltR = colorRGB1[0] - colorRGB2[0]
    deltG = colorRGB1[1] - colorRGB2[1]
    deltB = colorRGB1[2] - colorRGB2[2]
    interVal = 2*(deltR**2) + 4*(deltG**2) + 3*(deltB**2) + (r*(deltR**2-deltB**2))//256
    if interVal == 0:
        deltC = 0
    else: 
        deltC = math.sqrt(interVal)
    return deltC
 

def calculateRGBdiff(averageRGBlist):
	avgDiffList = [];
	for i in range(0, len(averageRGBlist)-1):
		deltC = calculatediffHelper(averageRGBlist[i], averageRGBlist[i+1])
		avgDiffList.append(deltC)
	return avgDiffList

def sortRGBDiff(avgDiffList):
    xList = []
    for i in range (0,len(avgDiffList)):
        if(avgDiffList[i] > 2):
            xList.append(i)
        print(avgDiffList[i])
    
    for j in range(0,len(xList)):
        img = cv2.line(img,(0,j),(1000,j),(0,0,255),2)
    
	



# ----------------- 
def main():
        img = readImageToRGB()
        averageRGBlist = avgRGBLine(img)
        avgDiffList = calculateRGBdiff(averageRGBlist)
        sortRGBDiff(avgDiffList)
        colorRGB1 = np.array((73,111,101))
        colorRGB2 = np.array((72,109,99))
        print(calculatediffHelper(colorRGB1,colorRGB2))
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
