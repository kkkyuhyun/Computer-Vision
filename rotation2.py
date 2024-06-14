import sys
import numpy as np
import cv2

#함수를 이용한 회전 확인. (함수를 사용하느냐 , 행렬을 사용하느냐 ) -> 2가지 방법이 존재한다. 
src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2) #이미지의 너비, 이미지의 높이
rot = cv2.getRotationMatrix2D(cp, 20, 1) #cp의 중심점에서 20도만큼 회전시키는 변환 행렬 

dst = cv2.warpAffine(src, rot, (0, 0))#src를 rot행렬에 따라 회전 시킨 결과 저장 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
