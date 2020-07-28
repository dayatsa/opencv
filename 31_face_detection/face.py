import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv.imread('messi5.jpg')
cam = cv.VideoCapture(0)

while cam.isOpened():
    ret, img = cam.read() 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in face:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
        
    cv.imshow('output', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()