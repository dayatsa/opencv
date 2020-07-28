import cv2

img = cv2.imread('foto.jpg',1)

print(img)

cv2.imshow('image', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

cv2.imwrite('foto_copy.png', img)