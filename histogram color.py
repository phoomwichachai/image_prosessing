import cv2
from matplotlib import pyplot as plt
image = cv2.imread('picture test.jpg')
color = ('Blue','Green','Red')
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.title('load histogram')
plt.show()
cv2.imshow('test', image)
cv2.waitKey(0)
