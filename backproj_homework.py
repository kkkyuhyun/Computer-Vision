import sys
import numpy as np
import cv2

# ���� ���� �ҷ�����
src = cv2.imread('bundang.jpg', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# �� ������ ���� �з��� �ҷ�����
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# �� ���� ����
faces = face_cascade.detectMultiScale(src, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# ���� ������� ������ ����
if len(faces) == 0:
    print('Face detection failed!')
    sys.exit()

# ����� �󱼿� ���� ����ũ ����
mask = np.zeros(src.shape[:2], dtype=np.uint8)
for (x, y, w, h) in faces:
    cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)  # �� �κ��� ������� ä��

# BGR���� YCrCb ���������� ��ȯ
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# CrCb ��� ������׷� ���ϱ�
channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([src_ycrcb], channels, mask, [128, 128], ranges)
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# �Է� ���� ������׷� ������ ����
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

# ������ ����� ����ũ�� �����Ͽ� �� �κи� ����
face_only = cv2.bitwise_and(src, src, mask=mask)

# ��� ���
cv2.imshow('src', src)
cv2.imshow('face_only', face_only)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
