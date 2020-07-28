import numpy as numpy
import cv2 as cv

img = cv.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in xrange(5):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)

layer = gp[-1]
cv.imshow('upper level Gaussian Image', layer)
lp = [layer]

for i in xrange(4,0,-1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)


cv.imshow('Original image', img)
cv.waitKey(0)
cv.destroyAllWindows()