import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def regionOfInterest(image, vertices):
    mask = np.zeros_like(image)
    # channel_count = image.shape[2]
    # match_mask_color = (255,)*channel_count
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv.bitwise_and(image, mask)
    return masked_img

def drawLines(image, lines):
    img_copy = np.copy(image)
    line_image = np.zeros((img_copy.shape[0], img_copy.shape[1], 3), dtype=np.uint8)
    
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(line_image, (x1,y1), (x2,y2), (0,255,0), 3)

    img_copy = cv.addWeighted(img_copy, 0.8, line_image, 1, 0.0)
    return img_copy


img = cv.imread('road1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

print(img.shape)
height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]

gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
canny_img = cv.Canny(gray_img, 100, 200)
cropped_img = regionOfInterest(canny_img,
              np.array([region_of_interest_vertices], np.int32),)
lines = cv.HoughLinesP(cropped_img, 6, np.pi/60, 160, np.array([]), 40, 25)
image_with_lines = drawLines(img, lines)

plt.imshow(image_with_lines)
plt.show()



# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()