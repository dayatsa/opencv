import cv2 as cv
import numpy as np

cam = cv.VideoCapture('vtest.avi')
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)

while cam.isOpened():
    ret, frame = cam.read()
    if frame is None:
        break
    fgmask =  fgbg.apply(frame) 
    # fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)  

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)
        
    keyboard = cv.waitKey(30)    
    if keyboard == 27 or keyboard == ord('q'):
        break

cv.destroyAllWindows()
cam.release()