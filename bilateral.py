#����� ���͸�

import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCLAE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)#src, -1 ����� ����, 10 ���� ����� ���� �ڵ� sigma space ũ��, 5 ���� ���� ũ�� ���� sigma color 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
 
cv2.destroyAllWindows()
