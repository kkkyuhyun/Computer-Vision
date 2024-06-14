import sys
import numpy as np
import cv2


src = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
#th�� �Ӱ谪, dst�� ����� ���� 
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # cv2.THRESH_OTSU�� �ڵ�ȭ�� �Ӱ� ������ �ǹ�.
print("otsu's threshold:", th)  # 131

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
#����� �������� �ڵ�����ȭ�� ������ ����ϴ� ���̴�. 