
import sys
import cv2

print("Hello OpenCV", cv2.__version__)

img = cv2.imread('cat.bmp')

if img is None:
    print('Failed to load image')
    sys.exit()

cv2.namedWindow('img1', cv2.WINDOW_NORMAL)
cv2.imshow('img1', img)

cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.imshow('img2', img)

cv2.namedWindow('img3', cv2.WINDOW_NORMAL)
cv2.imshow('img3', img)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.destroyAllWindows()

#import numpy as np
#import cv2

# ������ â ����
#img1 = np.full((240, 320, 3), (0, 0, 255), dtype=np.uint8)

# ���λ� â ����
#img2 = np.full((240, 320, 3), (0, 255, 0), dtype=np.uint8)

# �Ķ��� â ����
#img3 = np.full((240, 320, 3), (255, 0, 0), dtype=np.uint8)

# ������ �̹����� â���� ����
#cv2.imshow('Red Window', img1)
#cv2.imshow('Lime Window', img2)
#cv2.imshow('Blue Window', img3)

# Ű �Է��� ��ٸ� �� ��� â �ݱ�
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#import numpy as np
#import cv2


# ��� ����� �̹��� ����
#img = np.full((400, 400, 3), 255, np.uint8)

# �̹����� ������ �� �׸��� (BGR ���� �ڵ�: (0, 0, 255))
#cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)

# �̹����� ��ο� ������ �� �׸��� (BGR ���� �ڵ�: (0, 0, 128))
#cv2.line(img, (50, 50), (150, 160), (0, 0, 128), 5)

# �̹����� 'Image with Lines'��� �̸��� â���� ǥ��
#cv2.imshow('Image with Lines', img)

# Ű �Է��� ��ٸ� �� ��� â �ݱ�
#cv2.waitKey(0)
#cv2.destroyAllWindows()



