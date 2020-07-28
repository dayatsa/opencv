import cv2 as cv
import numpy as np

cam = cv.VideoCapture('vtest.avi')

ret, frame1 = cam.read()
ret, frame2 = cam.read()

while cam.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    _, contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour_ in contours:
        (x, y, w, h) = cv.boundingRect(contour_)
        if cv.contourArea(contour_) < 900:
            continue
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), thickness=2)
        cv.putText(frame1, "Status: {}".format('Movement'), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    # cv.drawContours(frame1, contours, -1, (0,255,255), thickness=2) 

    cv.imshow('inter', frame1)
    frame1 = frame2
    ret, frame2 = cam.read() 

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
cam.release()