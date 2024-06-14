import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200], #x���� 200��ŭ, y���� 100��ŭ �̵���Ų��. 
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
#src ������ �ִ� �����̹����� ������ ��ȯ��Ŀ� ���Ͽ� affine�̵���Ų �������ŭ ��Ÿ�� ����̴�. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
