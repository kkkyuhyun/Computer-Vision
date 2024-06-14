#양방향 필터링

import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCLAE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)#src, -1 양방향 필터, 10 필터 적용된 공간 자동 sigma space 크기, 5 색상 공간 크기 지정 sigma color 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
 
cv2.destroyAllWindows()
