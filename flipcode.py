import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
dst2=cv2.flip(src,-1,dst=None) 
#flip�̶�� �Լ��� �̿��Ͽ� �����¿� ��Ī�� ���� �� �ִ�. ����϶� �¿�, 0�϶� ����, �����϶� �¿���� 
dst3=cv2.flip(src,1,dst=None)
dst4=cv2.flip(src,0,dst=None)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()
cv2.destroyAllWindows()