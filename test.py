# -*- coding: utf-8 -*-

import cv2

# ���콺 Ŭ�� �̺�Ʈ �ݹ� �Լ�
def mouse_callback(event, x, y, flags, param):
    # ���콺 ���� ��ư�� Ŭ���� ��
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"which: ({x}, {y})")

# �̹��� ���� �б�
image = cv2.imread("tag.png")

# ������ ���� �� �̹��� ǥ��
cv2.namedWindow("image")
cv2.imshow("image", image)

# ���콺 �̺�Ʈ �ݹ� �Լ� ���
cv2.setMouseCallback("image", mouse_callback)

# Ű �Է� ���
cv2.waitKey(0)

# ������ ����
cv2.destroyAllWindows()