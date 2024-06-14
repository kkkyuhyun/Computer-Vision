import numpy as np
import cv2

img1=cv2.imread('HappyFish.jpg')
img2=img1
img3=img1.copy() #img3는 복사본
img1.fill(255)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitkey()
cv2.destroyAllWindows()
