import cv2
import numpy as np
image = cv2.imread('mess up pic.png')
kernel190 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
filterrimg190 = cv2.filter2D(image, -1, kernel190)
blur = cv2.blur(filterrimg190 , (9,9))
cv2.imshow('original iage', image)
cv2.imshow('filterrimg190', filterrimg190)
cv2.waitKey(0)
cv2.destroyAllWindows()