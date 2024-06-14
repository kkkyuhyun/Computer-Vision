# -*- coding: utf-8 -*-

import sys
import math
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

rad = 45 * math.pi / 180 #각도를 radian으로 표시 ->45도만큼 이동시키겠다. 
aff = np.array([[math.cos(rad), math.sin(rad), 0],  #->2*3행렬 중요!
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32) #기본값은 실수형이다(★중요) warpAfiine 행렬
#이동, 전단, 2*3의 행렬값 영상을 기하학적으로 변환시키고 있다.
dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
