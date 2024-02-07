import cv2
import numpy as np
image = cv2.imread('cameraman.jpg')
blur = cv2.blur(image, (5,5))
kernel45 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel190 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
filterrimg45 = cv2.filter2D(image, -1, kernel45)
filterrimg190 = cv2.filter2D(image, -1, kernel190)
cv2.imshow('original image', image)
cv2.imshow('filterrimg45', filterrimg45)
cv2.imshow('filterrimg190', filterrimg190)
cv2.waitKey(0)
cv2.destroyAllWindows()