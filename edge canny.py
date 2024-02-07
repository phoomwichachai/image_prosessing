import cv2
image = cv2.imread('cameraman.jpg')
gray = cv2.cvtColor(image, 0)
blur = cv2.GaussianBlur(gray, (3,3), 0)
lowerT = 75
upperT = 150
canny = cv2.Canny(blur, lowerT, upperT)
cv2.imshow('original image', image)
cv2.imshow('canny() function', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()