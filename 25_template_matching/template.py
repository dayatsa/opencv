import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg')
grey_img =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('messi_face.png', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(grey_img, template, cv.TM_CCOEFF_NORMED)
print(res)
thresh = 0.91 ;
loc = np.where(res >= thresh)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imshow('image', img)
    
cv.waitKey(0)
cv.destroyAllWindows()