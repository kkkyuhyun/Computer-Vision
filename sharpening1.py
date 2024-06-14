import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE) #�ҽ��̹���

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2) #�ε巯������ ���ؼ� ��ó���� �Ѵ�. (�ھ˰��� ����ϱ�!)
dst1 = cv2.subtract(src,blr) #subtract�� ���Ͽ� �����̹��� - ��ó���̹��� = ������ ������ CV07 p.28 �Լ����� �ð�(��ǥ��)�� �κ� ���� ��µ� ��. 
dst2 = cv2.addWeighted(src,1, blr,-1, 128)#src, 1ù��° �̹��� ����ġ, blr �ι�° �Է� �̹��� ����þ� ����, -1 �ι�° �̹��� ����ġ , 128 ��� �̹��� �߰� ���� �� ��� ����
dst3 = cv2.addWeighted(src,2, blr,-1, 0) #��°�� �������� �� �ѷ������� Ȯ���� �� �ִ�. addweighted�� 0�� ����ϸ� �� ó���� ����� sharp�� ��µȴ�. 
dst4 = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)#��°�� �������� �� �ѷ������� Ȯ���� �� �ִ�. # src �տ� ����� �� ������ ���� �Ͼ���� �� �����ȴ�. 


cv2.imshow('src', src)
cv2.imshow('blr',blr)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()

cv2.destroyAllWindows()
