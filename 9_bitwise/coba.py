import cv2
import numpy as nn

img1 = nn.zeros((250,500,3), nn.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)

cv2.imshow('image', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
