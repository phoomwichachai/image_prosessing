import cv2
cap = cv2.VideoCapture('myreccord.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print(f"problem with frame")
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()