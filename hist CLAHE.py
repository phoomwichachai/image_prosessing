import cv2
from matplotlib import pyplot as plt
image = cv2.imread('picture test.jpg', 0)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
clahe = cv2.createCLAHE()
cl1 = clahe.apply(image)
CLAHEisteq = cv2.calcHist([cl1], [0], None, [256], [0, 256])
cv2.imshow('load image', image)
cv2.imshow('CLAHE', cl1)
plt.plot(hist)
plt.title('histogram')
plt.show()
plt.plot(CLAHEisteq)
plt.title('CLAHE hist')
plt.show()
cv2.waitKey(0)