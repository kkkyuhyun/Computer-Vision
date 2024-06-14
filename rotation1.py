# -*- coding: utf-8 -*-

import sys
import math
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

rad = 45 * math.pi / 180 #������ radian���� ǥ�� ->45����ŭ �̵���Ű�ڴ�. 
aff = np.array([[math.cos(rad), math.sin(rad), 0],  #->2*3��� �߿�!
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32) #�⺻���� �Ǽ����̴�(���߿�) warpAfiine ���
#�̵�, ����, 2*3�� ��İ� ������ ������������ ��ȯ��Ű�� �ִ�.
dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
