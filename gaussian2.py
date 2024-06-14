# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

for sigma in range(1, 6): ###sigma�� 1���� 5���� ��ȸ���� ����� �����Ѵ�. �ñ׸� ���� ���� �ε巯�� �̹����� �����.
    # sigma ���� �̿��Ͽ� ����ð� ���͸�
    dst = cv2.GaussianBlur(src, (0, 0), sigma)

    desc = 'sigma = {}'.format(sigma)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA) #cv2.putText(�߰��̹���, ǥ���ؽ�Ʈ ����, �ؽ�Ʈ ��ǥ, �ؽ�Ʈ ��Ʈ, �ؽ�Ʈ ũ��, ��, �ؽ�Ʈ �β�, ����Ÿ��)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
