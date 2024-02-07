import cv2
import numpy as np
KERNEL_1 = 25


image = cv2.imread('mess up pic.png')
blur = cv2.medianBlur(image, KERNEL_1)
kernel45 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
filterrimg190 = cv2.filter2D(blur, -1, kernel45)



cv2.imshow('image clear one', filterrimg190)
cv2.imshow('original image', image)
cv2.imshow(f'median blur kernel size {KERNEL_1}', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()