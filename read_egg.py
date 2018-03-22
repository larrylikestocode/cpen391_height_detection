import cv2
import numpy as np

imgBGR = cv2.imread('image_face.jpg')
destRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
sampleColor = destRGB[1][1]
print(destRGB[1])
for i in range(500):
    for j in range(500):
        if(destRGB[i][j] == sampleColor):
            print("face detected")
