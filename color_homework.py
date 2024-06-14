import numpy as np
import cv2

img1 = np.full((240,240,3),(0,0,255),dtype=np.uint8)
img2 = np.full((240,240,3),(255,0,0),dtype=np.uint8)
img3 = np.full((240,240,3),(0,255,0),dtype=np.uint8)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

while True:
    if cv2.waitKey() == ord('q'):
        break
    cv2.destroyAllWindows()