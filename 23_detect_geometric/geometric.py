import numpy as np
import cv2 as cv

img = cv.imread('shapes.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgGray, 240, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour_ in contours:
    approx = cv.approxPolyDP(contour_, 0.01*cv.arcLength(contour_, True), True)
    cv.drawContours(img, [approx], 0, (0,0,0), 3)
    x = approx.ravel()[0] - 5
    y = approx.ravel()[1] 
    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0)) 
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        ratio = float(w)/h
        print(ratio)
        if ratio >= 0.95 and ratio <= 1.05:
            cv.putText(img, 'Rectangle', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0)) 
        else:
            cv.putText(img, 'Rectangle', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0)) 
    
    elif len(approx) == 5:
        cv.putText(img, 'Pentagon', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0)) 
    else:
        cv.putText(img, 'Circle', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0)) 

cv.imshow('image', img)
cv.imshow('thresh', thresh)
cv.waitKey(0)
cv.destroyAllWindows()