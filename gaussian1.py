import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.GaussianBlur(src, (0, 0), 7) #맨 마지막 값 시그마 값을 올릴 수록 blurr가 더 강하게 표시 된다.
dst2 = cv2.blur(src, (7, 7))#src이미지에 7*7크기의 블러링을 적용한다.커널크기가 클수록 blur도 커진다.
#각각의 sigma값에따라 blur효과가 있다. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
