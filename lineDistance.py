import cv2
import numpy as np
import time
import math 
# TBD
# face3 val 
BEGINX = 0
BEGINY = 0
ENDX = 0
ENDY = 1000
#THRESHHOLD = 9

# face4 val
#BEGINX = 0
#BEGINY = 550
#ENDX = 0
#ENDY = 650
COLORDIFF_THRESHHOLD = 3 # tested max for face3.jpg
FOREHEAD_THRESHHOLD = 85 # TBD
FILE_NAME = "photos/test_pic27.jpg"
FACE_CASCADE = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')

# ----------------- 
def readImageToRGB(fileName):
	imgBGR = cv2.imread(fileName)
	imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
	return imgRGB



# ---------------------
# return a coordinate for finding the recbox of the box
def faceRec(fileName):
    face_cord =[]
    img = cv2.imread(fileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(gray,1.3,5)
    
    # BeginCol EndCol BeignRow EndRow
    for(x,y,w,h) in faces:    
        face_cord.append(x)
        face_cord.append(x+w)
        face_cord.append(y)
        face_cord.append(y+h)
    if(len(face_cord) == 0):
        print("No face detected")
    return face_cord


# -----------------
# return a list of averge RGB values per line of the image 
def avgRGBLine(imgRGB, faceCord):
    global BEGINY
    global ENDY
    height = imgRGB.shape[0]
    width  = imgRGB.shape[1]
    avglist=[];
    if(len(faceCord) != 0):
        BEGINY = faceCord[0]
        ENDY = faceCord[1]
        maxX = faceCord[3]
    else:
        maxX = height
        BEGINY = 0
        ENDY = width
    for x in range (0, maxX):
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
 
# -----------------
# finding all the colordiff val for selected rows
def calculateRGBdiff(averageRGBlist):
	avgDiffList = [];
	for i in range(0, len(averageRGBlist)-1):
		deltC = calculatediffHelper(averageRGBlist[i], averageRGBlist[i+1])
		avgDiffList.append(deltC)
	return avgDiffList

# -----------------
# Need to modify
def sortRGBDiff(avgDiffList,imgRGB, face_cord):
    xList = []
    foreheadLine = face_cord[2]
    cv2.putText(imgRGB, 'foreheadLine',(face_cord[0],foreheadLine),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),1,cv2.LINE_AA)
    imgRGB = cv2.line(imgRGB,(BEGINY,foreheadLine),(ENDY,foreheadLine),(255,0,0),2)

    cv2.putText(imgRGB, 'forehead threshhold Line',(face_cord[0],foreheadLine-FOREHEAD_THRESHHOLD),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),1,cv2.LINE_AA)
    imgRGB = cv2.line(imgRGB,(BEGINY,foreheadLine-FOREHEAD_THRESHHOLD),(ENDY,foreheadLine-FOREHEAD_THRESHHOLD),(255,0,0),2)
    
    markXh = foreheadLine
    for i in range (foreheadLine-FOREHEAD_THRESHHOLD,len(avgDiffList)):
        colorDiff = avgDiffList[i]
        print(colorDiff)
        # check if the colordiff is above the preset threshhold 
            # check if     
        if(i <= foreheadLine and i >= foreheadLine-FOREHEAD_THRESHHOLD):
            if(colorDiff > COLORDIFF_THRESHHOLD):
                imgRGB = cv2.line(imgRGB,(BEGINY,i),(ENDY,i),(0,0,255),2)
                markXh = i
                break
        else:
            markXh = foreheadLine
            break
#            imgRGB = cv2.line(imgRGB,(BEGINY,i),(ENDY,i),(0,0,255),2)

    j = foreheadLine
    markXl = foreheadLine
    while j >= foreheadLine-FOREHEAD_THRESHHOLD:
        j = j -1
        colorDiffL = avgDiffList[j]
        if(colorDiffL > COLORDIFF_THRESHHOLD):
#            imgRGB = cv2.line(imgRGB,(BEGINY,j),(ENDY,j),(0,0,255),2)
            markXl = j
            break
        else:
            markXl = foreheadLine

        
    heightLinev = (markXl + markXh)//2
    print("the height of the person is" + str(heightLinev))
    print("the hight hight is" + str(markXh))
    
    cv2.putText(imgRGB, 'markedLinehigh',(face_cord[0],markXh),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,0),1,cv2.LINE_AA)    
    imgRGB = cv2.line(imgRGB,(BEGINY,markXh),(ENDY,markXh),(0,0,255),2)

    cv2.putText(imgRGB, 'markedLineLow',(face_cord[0],markXl),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,0),1,cv2.LINE_AA)    
    imgRGB = cv2.line(imgRGB,(BEGINY,markXl),(ENDY,markXl),(0,0,255),2)
    
    cv2.putText(imgRGB, 'hight',(face_cord[0],heightLinev),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,0),1,cv2.LINE_AA)    
    imgRGB = cv2.line(imgRGB,(BEGINY,heightLinev),(ENDY,heightLinev),(0,0,255),2)
    
    
    # print linr has the best difference
    imgRGB = cv2.rectangle(imgRGB,(BEGINY,0),(ENDY,1200),(255,0,0),2)
    imgBGR = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow('img',imgBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
#    cv2.imwrite("photos/color_line.jpg",imgBGR)
    return xList

# ----------------- 
def main():
        img = readImageToRGB(FILE_NAME)
        
        faceCord = faceRec(FILE_NAME)
        
        averageRGBlist = avgRGBLine(img, faceCord)
        
        avgDiffList = calculateRGBdiff(averageRGBlist)

        xList = sortRGBDiff(avgDiffList, img,faceCord)
        
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
