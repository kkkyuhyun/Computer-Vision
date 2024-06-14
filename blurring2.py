import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

for ksize in (3, 5, 7): #ksize�� 3,5,7�� ��ȸ�Ͽ� 
    dst = cv2.blur(src, (ksize, ksize)) #3*3ũ���� Ŀ���� ���� ũ��� ���� ������ ����� ���δ�. 
    desc = 'Mean: {}x{}'.format(ksize, ksize) #desc�� ���� ũ�⿡ ǥ���ϴ� ���ڿ��� �����Ѵ�. 
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                
#cv2.putText(�̹���, ǥ�� �ؽ�Ʈ,  �ؽ�Ʈ ��ǥ, �ؽ�Ʈ ��Ʈ ��Ÿ��, �ؽ�Ʈ ũ��, ���� �ؽ�Ʈ �β�, �ε巴�� )
                1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
