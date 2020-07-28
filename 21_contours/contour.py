import numpy as np
import cv2 as cv

img = cv.imread('opencv-logo.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# _, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
_, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print('Number of contours : ', str(len(contours)))

cv.imshow('image', img)
cv.imshow('image gray', thresh)
cv.waitKey(0)
cv.destroyAllWindows()