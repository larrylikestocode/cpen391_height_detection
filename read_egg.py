import cv2
import numpy as np

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
