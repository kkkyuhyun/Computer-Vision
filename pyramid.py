# -*- coding: utf-8 -*-��


import sys
import numpy as np
import cv2


src = cv2.imread('cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# ��������׸���
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# �Ƕ�̵念��׸���
for i in range(1, 4): #�ݺ����� Ȱ���Ͽ� �پ���� Ȯ���� �� �ִ�. 
    src = cv2.pyrDown(src) #�Ź� ��� X Ư���� ��� ������� �� �� �ִ�. �ٿ���ø� �����ø��� �Ѵٸ� ����.
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)#(�̹���, �簢��, ����, �簢�� ���� �β� ���� ���� i�� 1���� 3����)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
