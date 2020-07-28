import numpy as np
import cv2 as cv

img = cv.imread('gradient.png')
ret, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) 
ret, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) 
ret, th3 = cv.threshold(img, 150, 255, cv.THRESH_TRUNC) 
ret, th4 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO) 
ret, th5 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO_INV) 


cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)

cv.waitKey(0)
cv.destroyAllWindow()