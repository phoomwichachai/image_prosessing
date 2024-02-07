import cv2
cap = cv2.VideoCapture(0)
currentFrame = 0
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
codec = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('myreccord.avi', codec, 24.0, (int(width), int(height)))

while cap.isOpened():
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    out.write(frame)
    cv2.imshow('Live webcam', frame)
    if cv2.waitKey(1)==27:
        break
    currentFrame += 1
cap.release()
cap.release()
cv2.destroyAllWindows()