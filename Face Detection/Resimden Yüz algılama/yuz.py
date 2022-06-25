import cv2

img=cv2.imread("face.png")
img2=cv2.imread("face2.jpg")

face_cascade=cv2.CascadeClassifier("frontalface.xml")

gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,),2)

cv2.imshow("Fce",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

