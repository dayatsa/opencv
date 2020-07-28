import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.png',0)
ret, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) 
ret, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) 
ret, th3 = cv.threshold(img, 150, 255, cv.THRESH_TRUNC) 
ret, th4 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO) 
ret, th5 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO_INV) 

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in xrange(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# cv.imshow('image', img)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
# cv.imshow('th5', th5)

plt.show()
cv.waitKey(0)
cv.destroyAllWindow()