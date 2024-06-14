import sys
import numpy as np
import cv2


src = cv2.imread('tag.png')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[85, 490], [618, 365], [809, 623], [229, 813]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

#���ú�ȯ: ���ٰ��� ����Ͽ� �̹����� ��ȯ�ϴ� ���, ���� ȿ�� ����
#���ú�ȯ: 3*3 ��ķ� 4���� �Է� ���� �ش� ���� ���� 4�� ��� �� ���
#�����κ�ȯ: �̹��� ũ�� ���� �̵� ����� ��ȯ ���� ȿ�� ���X ���� �� ���� �̹��� ��ȯ
#�����κ�ȯ:2*3��ķ� 3���� �Է� ���� �ش� ���� ���� 3�� ��� �� ���
# > ���ú�ȯ�� ���� ȿ���� �����ϰ�, �����κ�ȯ�� ���� �� ���� �̹��� ��ȯ 


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
