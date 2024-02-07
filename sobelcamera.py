import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame', cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    sobelxy = cv2.bitwise_or(sobelx, sobely)
    sobelxy = cv2.convertScaleAbs(sobelxy)
    cv2.imshow('Webcam sobel frame', sobelxy)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()