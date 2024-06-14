import sys
import numpy as np
import cv2

src=cv2.imread('Hawkes.jpg',cv2.IMREAD_GRAYSCALE)

if src is None:
    print("failed to load image")
    sys.exit()
    
dst=cv2.equalizeHist(src)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows() 