import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2] # �̹����� ���̿� �ʺ� Ʃ�÷� ��ȯ.  h���� �̹����� ���̰�, w���� �̹����� �ʺ� ����˴ϴ�.

map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)
#np.indices((h, w), dtype=np.float32):
#np.indices() �Լ��� �־��� ���� h�� �ʺ� w�� ���� ��ǥ ������ �����մϴ�.
#��ȯ�� ����� �� ���� �迭�� �����˴ϴ�: map1�� map2.
#dtype=np.float32�� �迭 ����� ������ Ÿ���� 32��Ʈ �ε��Ҽ������� �����մϴ�.
#map2 = map2 + 10 * np.sin(map1 / 32):
#map1 �迭�� x�� ��ǥ�� ��Ÿ����, map2 �迭�� y�� ��ǥ�� ��Ÿ���ϴ�.
#np.sin(map1 / 32)�� map1 �迭�� �� ��ҿ� ���� ���� �Լ��� ����մϴ�.
#�̷��� ���� ���� ���� 10�� ���� �� map2 �迭�� ���մϴ�.
#�̷��� ������ map1�� map2 �迭�� �̹��� ��ȯ�� ���Ǹ�, ��ǥ ������ ���� �̹����� �̵��ϰų� �ְ��ų �� �ֽ��ϴ�.
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)
print(map1[0:4])
print(map2[0:4])
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

#������ �ֿ� ����
#�̹��� ��ȯ (Image Transformation):
#��ǥ ������ �̹����� ��ȯ�ϴ� �� ���˴ϴ�. ��ȯ���� ũ�� ����, ȸ��, �̵�, �ְ� ���� ���Ե˴ϴ�.

#�κ� ��� (Region of Interest, ROI):

#ROI�� �����ϰ� �ش� �κ��� �ٸ� �̹����� �����ϰų� �ٿ����� �� ��ǥ ������ �ʿ��մϴ�.
#�ְ� ���� (Distortion Correction):
#ī�޶� ���� �ְ��� �����ϱ� ���� ��ǥ ������ ����մϴ�.
#���� �ְ��� �����ϰ� �̹����� ��Ȯ�ϰ� ǥ���ϱ� ���� ��ǥ�� �����մϴ�.
#Ư�� ȿ�� (Special Effects):
#��ǥ ������ �̹����� Ư�� ȿ���� �����ϴ� �� ���˴ϴ�.