import cv2
image = cv2.imread('picture test.jpg', 1)
blur9 = cv2.blur(image, (9,9))
blur15 = cv2.blur(image, (15,15))
cv2.imshow('original image', image)
cv2.imshow('blur9', blur9)
cv2.imshow('blur15', blur15)
cv2.waitKey(0)
cv2.destroyAllWindows()
