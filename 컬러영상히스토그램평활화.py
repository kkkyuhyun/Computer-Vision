import sys
import numpy as np
import cv2

# �̹����� �ҷ��ɴϴ�.
src = cv2.imread('field.bmp')

# �̹����� ����� �ҷ��������� Ȯ���մϴ�.
if src is None:
    print("failed to load image")
    sys.exit()

# BGR���� YCrCb ���������� ��ȯ�մϴ�.
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# YCrCb ä���� �и��մϴ�.
ycrcb_planes = cv2.split(src_ycrcb)

# Y ä���� ������׷��� �յ�ȭ�մϴ�.
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

# �յ�ȭ�� ä���� �ٽ� ��Ĩ�ϴ�.
dst_ycrcb = cv2.merge(ycrcb_planes)

# YCrCb���� BGR ���������� ��ȯ�մϴ�.
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR) 

# ���� �̹����� ��� �̹����� �����ݴϴ�.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()  # ��� â�� �ݽ��ϴ�.
