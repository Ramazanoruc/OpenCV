import cv2

vid=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("frontalface.xml")

while 1:
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.1,20)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,"Ramazan",(x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    cv2.imshow("Fce",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    print(frame)

vid.release()
cv2.destroyAllWindows()