import cv2 as cv
import numpy as np

cam = cv.VideoCapture('traffic.mp4')

ret, frame = cam.read()
x,y,width,height = 465, 133, 40, 20

track_window = (x,y,width,height)

roi = frame[y:y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
term_crit = (cv.TERM_CRITERIA_EPS | cv.TermCriteria_COUNT, 10, 1)

cv.imshow('roi', roi)
while cam.isOpened():
    ret, frame = cam.read()
    if frame is None:
        break
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    ret, track_window = cv.CamShift(dst, track_window, term_crit)    
    
    pts = cv.boxPoints(ret)
    print(pts)
    pts = np.int0(pts)
    final_image = cv.polylines(frame, [pts], True, (0, 255, 0), 2)

    # x,y,w,h = track_window
    # final_image = cv.rectangle(frame, (x,y), (x+w, y+h), 255, 3)
    
    cv.imshow('dst', dst)
    cv.imshow('final_image', final_image)
        
    keyboard = cv.waitKey(30)    
    if keyboard == 27 or keyboard == ord('q'):
        break

cv.destroyAllWindows()
cam.release()