import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img = cv.imread('messi5.jpg')
cam = cv.VideoCapture(0)

while cam.isOpened():
    ret, img = cam.read() 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in face:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)
        
    cv.imshow('output', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()