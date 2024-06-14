import sys
import cv2

# �̹��� ������ �ҷ��ɴϴ�.
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

# �̹��� ������ ����� �ҷ��������� Ȯ���մϴ�.
if src is None or mask is None or dst is None:
    print('Image load failed')
    sys.exit()

# mask�� ����Ͽ� src�� Ư�� �κ��� dst�� �����մϴ�.
cv2.copyTo(src, mask, dst)

# ��� �̹����� ȭ�鿡 ǥ���մϴ�.
cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

# Ű �Է��� ��ٸ� �� ��� â�� �ݽ��ϴ�.
cv2.waitKey()
cv2.destroyAllWindows()
