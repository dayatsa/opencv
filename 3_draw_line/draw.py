import cv2
import numpy as nn
#img = cv2.imread('foto.jpg',1)
img = nn.zeros([512,512,3], nn.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,255), 5)
img = cv2.arrowedLine(img, (100,0), (255,255), (255,255,255), 5)

img = cv2.rectangle(img, (500,350), (300,300), (0,0,255), 3)
img = cv2.circle(img, (333,333), 50, (0,255,0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (500,100), font, 1, (255,255,255), 3, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
