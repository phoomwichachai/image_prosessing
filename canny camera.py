import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame', cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    canny = cv2.Canny(gray, 50, 150)
    cv2.imshow('Webcam canny frame', canny)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()