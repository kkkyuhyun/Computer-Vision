import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

kernel = np.ones((3, 3), dtype=np.float64) / 9. #3*3ũ���� ��� ��Ҹ� 9�� ������ ����� ����Ѵ� 
dst = cv2.filter2D(src, -1, kernel) #2D���͸� �����ϴ� �ڵ�� Src�� Ŀ���� �����Ͽ� ����� �����Ѵ�. (src, depth, kernel)
dst = cv2.blur(src, (3, 3)) #src�̹����� 3*3ũ�� �����Ѵ�. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
