import cv2

image = cv2.imread('picture test.jpg', 0)
cv2.imshow('load image', image)
ret, thresh1 = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('threshhold image', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()