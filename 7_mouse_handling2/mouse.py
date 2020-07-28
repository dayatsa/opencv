import numpy as nn
import cv2

# events = {i for i in dir(cv2) if 'EVENT' in i}
# print(events)

def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 3)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)

        mycolor = nn.zeros((512,512,3), nn.uint8)
        mycolor[:] = [blue, green, red]

        cv2.imshow('color', mycolor)
    

# img = nn.zeros((512,512,3), nn.uint8)
img = cv2.imread('foto.jpg')
cv2.imshow('image', img)

points = []
cv2.setMouseCallback('image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()