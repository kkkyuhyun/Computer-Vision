import sys
import cv2

# 이미지 파일을 불러옵니다.
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

# 이미지 파일이 제대로 불러와졌는지 확인합니다.
if src is None or mask is None or dst is None:
    print('Image load failed')
    sys.exit()

# mask를 사용하여 src의 특정 부분을 dst에 복사합니다.
cv2.copyTo(src, mask, dst)

# 결과 이미지를 화면에 표시합니다.
cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

# 키 입력을 기다린 후 모든 창을 닫습니다.
cv2.waitKey()
cv2.destroyAllWindows()
