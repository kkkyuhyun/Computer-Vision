import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# �̹����� ������� �о���Դϴ�.
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)


# �̹����� ����� �ε�Ǿ����� Ȯ���մϴ�.
if src is None:
    print('Image load failed')
    sys.exit()

# ������׷��� ����մϴ�.
hist = cv2.calcHist([src], [0], None, [256], [0, 256])#calcHist(�Է�, ����ε���, ����ũ����, histsize, histrange)

# ���� �̹����� ȭ�鿡 ǥ���մϴ�.
cv2.imshow('src', src)
cv2.waitKey(1)

# ������׷��� �׷����� ǥ���մϴ�.
plt.plot(hist)
plt.show()