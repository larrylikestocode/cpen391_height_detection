import cv2
import numpy as np



# A filter helper function
def filter_RGB:
	 blue, green, red = cv2.split(img)
	 cv2.ShowImage("Blue",blue)
	 cv2.ShowImage("Green", green)
	 cv2.ShowImage("Red", red)



# iterate through the matrix
def iterate_Img:
	img = cv2.imread('photos/girl_brownBackground.jpg')
	# version 1
	for i in range(im.height):
    	for j in range(im.width):
        	im[i,j] #Do whatever you want with your pixel


    # version 2
    img = cv2.imread('photos/girl_brownBackground.jpg')
    li = cv.InitLineIterator(im, (0, 0), (im.rows, im.cols)) #So loop the entire matrix

	for (r, g, b) in li:
  
imgBGR = cv2.imread('photos/girl_brownBackground.jpg')
destRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
#print(destRGB)
print(destRGB.shape)
print(destRGB.max())
print(destRGB[2,3])
#sampleColor = destRGB[1][1]
#print(destRGB[1])
#for i in range(500):
#    for j in range(500):
#        if(destRGB[i][j] == sampleColor):
#            print("face detected")
