import sys
import numpy as np
import cv2

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3)#3*3크기의 중간값 블러링 처리 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

#중간값 블러는 주변 픽셀 중간값을 사용해서 현재 픽셀을 대체하는 방식이다.
#노이즈 제거에 효과적인 필터링 기법이다. 
