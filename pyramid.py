# -*- coding: utf-8 -*-ㅠ


import sys
import numpy as np
import cv2


src = cv2.imread('cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본영상그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드영상그리기
for i in range(1, 4): #반복문을 활용하여 줄어듦을 확인할 수 있다. 
    src = cv2.pyrDown(src) #매번 사용 X 특수한 경우 사용함을 알 수 있다. 다운샘플링 업샘플링을 한다만 알자.
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)#(이미지, 사각형, 빨강, 사각형 선의 두께 변경 조절 i는 1부터 3까지)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
