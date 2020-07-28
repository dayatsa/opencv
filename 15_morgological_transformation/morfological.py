import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('smarties.png',cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)
dilation = cv.dilate(mask, kernel,iterations=2)
erotion = cv.erode(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)
print(kernel)

titles = ['image','mask','dilation', 'erotion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erotion, opening, closing, mg, th]

for i in xrange(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()