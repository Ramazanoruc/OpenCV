from ast import While
from tkinter import Frame
import cv2
from cv2 import VideoCapture
from cv2 import cvtColor
import numpy as np

cap=VideoCapture(0)   #Get image from webcam

def nothing(x):  #Trackbar has to give 5 parameters, so you have to declare null function
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",500,500)#Trackbar size

cv2.createTrackbar("Lower->H","Trackbar",0,180,nothing)#Define lower values
cv2.createTrackbar("Lower->S","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower->V","Trackbar",0,255,nothing)

cv2.createTrackbar("Upper->H","Trackbar",0,180,nothing)#Define upper values
cv2.createTrackbar("Upper->S","Trackbar",0,255,nothing)
cv2.createTrackbar("Upper->V","Trackbar",0,255,nothing)

cv2.setTrackbarPos("Upper->H","Trackbar",180)
cv2.setTrackbarPos("Upper->S","Trackbar",255)
cv2.setTrackbarPos("Upper->V","Trackbar",255)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_h=cv2.getTrackbarPos("Lower->H","Trackbar")
    lower_s=cv2.getTrackbarPos("Lower->S","Trackbar")
    lower_v=cv2.getTrackbarPos("Lower->V","Trackbar")

    upper_h=cv2.getTrackbarPos("Upper->H","Trackbar")
    upper_s=cv2.getTrackbarPos("Upper->S","Trackbar")
    upper_v=cv2.getTrackbarPos("Upper->V","Trackbar")

    lower_color=np.array([lower_h,lower_s,lower_v])
    upper_color=np.array([upper_h,upper_s,upper_v])

    mask=cv2.inRange(frame_hsv,lower_color,upper_color)
    cv2.imshow("Original",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    

