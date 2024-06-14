import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1) #dx dy ���ȭ ���״�. 

mag = cv2.magnitude(dx, dy) #magnitudeȭ
mag = np.clip(mag, 0, 255).astype(np.uint8) #clip���� �����ְ� type�� �Ǽ������� ���������� �ٲ��ְ� 
#�迭�� ������ Ÿ���� 32��Ʈ �ε��Ҽ������� 8��Ʈ ��ȣ ���� ������ ��ȯ. 
# �̷��� ��ȯ�ϸ� �ȼ� ���� ������ ǥ���Ǹ�, �̹����� ǥ���ϰų� ������ �� ���˴ϴ�.

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255 #�Ͼ������ 
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)
#magnitude�� 80���� ���߸� �� ���� ������ ����ȴ�. ������ �Ӱ谪�� ���߸� �� ���� �Ӱ谪 ����, ���̰� �ȴٸ� �Ʊ�� �� ���� ���� �� �ȴ�. 
#�׷����Ʈ ����. 
cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

#magnitude�� �� ����: �̹��� ��踦 �����ϰ� �ȼ� ���� ũ�⸦ �����ϱ� ����..