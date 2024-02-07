import cv2
from matplotlib import pyplot as plt
photo = cv2.imread('picture test.jpg', 0)
hist = cv2.calcHist([photo], [0], None, [256], [0, 256])
cv2.imshow('load image', photo)
cv2.waitKey(0)
plt.plot(hist)
plt.title('load image histogram')
plt.show()
cv2.waitKey(0)