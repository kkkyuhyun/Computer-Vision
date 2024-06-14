import sys
import numpy as np
import cv2

#�Լ��� �̿��� ȸ�� Ȯ��. (�Լ��� ����ϴ��� , ����� ����ϴ��� ) -> 2���� ����� �����Ѵ�. 
src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2) #�̹����� �ʺ�, �̹����� ����
rot = cv2.getRotationMatrix2D(cp, 20, 1) #cp�� �߽������� 20����ŭ ȸ����Ű�� ��ȯ ��� 

dst = cv2.warpAffine(src, rot, (0, 0))#src�� rot��Ŀ� ���� ȸ�� ��Ų ��� ���� 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
