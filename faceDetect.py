import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
cap = cv2.VideoCapture(0)
seq = "Hello"

def showSeq(seq, originalImg, grayImg):
    
    faces = face_cascade.detectMultiScale(grayImg, 1.3, 5)
    cv2.imshow("gray", grayImg)
    for(x,y,w,h) in faces:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(originalImg, seq, (x+w, y+h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
        cv2.rectangle(originalImg, (x,y), (x+w, y+h), (255,0,0), 2)
        
    return originalImg
    
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = showSeq(seq, img, gray)
    cv2.imshow("img", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
