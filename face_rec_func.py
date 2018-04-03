import cv2
import numpy as np

FACE_CASCADE = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
FILE_NAME = "photos/face4.jpg"


# ---------------------
# return a coordinate for finding the recbox of the box
def faceRec(fileName):
    face_cord =[]
    img = cv2.imread('photos/face3.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(gray,1.3,5)
    print(faces)
    for(x,y,w,h) in faces:
        endX =x+w
        endY =y+h
        print(x)
        print(y)
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # order beginY endY beginX endX  
#    face_cord.append(x)
#    face_cord.append(endX)
#    face_cord.append(y)
#    face_cord.append(endY)
#    cv2.imshow('img',imgBGR)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    print("beginCol: " +str(x) +" beginRow: " +str(y)+" endCol: " +str(x+w) +" endRow: " +str(y+h))
    return face_cord

faceRec(FILE_NAME)
