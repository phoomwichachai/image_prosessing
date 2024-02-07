import cv2
image = cv2.imread("picture test.jpg", 1)
B, G, R = cv2.split(image)
Blue1 = cv2.imwrite("Blue1.jpg", B)
if Blue1 == True:
    print(f'Written B image status: {Blue1}')
else:
    print(f'image B not saved')