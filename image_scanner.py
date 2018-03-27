import cv2
from numpy import unravel_index
import numpy as np




def read_image():
    imgBGR = cv2.imread('photos/face3.jpg')
    #destRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
    return imgBGR#destRGB


def scan_color_image(img):
    print("the height is: " + str(img.shape[0]/100))
    print("the width is: " + str(img.shape[1]/100))

    maxHeight = img.shape[0]
    maxWidth  = img.shape[1]

    paraA = 20
    paraB = 30
    
#    beginX = maxHeight//3 - paraA
#    beginY = (maxWidth//3)-paraB
#    endX   = maxHeight//3+paraA
#    endY   = maxWidth//3+paraB
    beginX = 650
    beginY = 260
    endX = 900
    endY = 320


    avg_rgb = np.array((0,0,0))

    
    for x in range(beginX,endX):
        avg_rgb = np.array((0,0,0))
        for y in range(beginY,endY):
            avg_rgb = avg_rgb + img[x][y]
            #print(img[x][y])

        print(str(endX) +" "+ str(endY))
        print("x value is"+str(x))
        print(avg_rgb//(endY-beginY))
        print("")
        
    # selected area
    img = cv2.rectangle(img,(beginX,beginY),(endX,endY),(255,0,0),2)
    # selected point draw a line across x axis 
    img = cv2.line(img,(854,0),(854,maxWidth),(0,0,255),2)
    cv2.imwrite("photos/analysis.jpg",img)
    

def main():
    print(cv2.__version__)
    rGb = read_image()
    scan_color_image(rGb)
    






main()
#    print(unravel_index(img.argmax(),img.shape)) #maximum
