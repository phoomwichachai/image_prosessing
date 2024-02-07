import cv2
image = cv2.imread("picture test.jpg", 1)
B = image[0:300,0:500,0]
G = image[:,:,1]
R = image[:,:,2]
cv2.imshow("picture that i like", image)
cv2.waitKey(0)
cv2.imshow("Blue picture that i like", B)
cv2.waitKey(0)
cv2.imshow("Green picture that i like", G)
cv2.waitKey(0)
cv2.imshow("Red picture that i like", R)
cv2.waitKey(0)
cv2.destroyAllWindows()
