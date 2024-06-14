import sys
import cv2

cap = cv2.VideoCapture('video1.mp4')

if not cap.isOpened():
    print("Camera open failed")
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
