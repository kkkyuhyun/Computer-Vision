import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2] # 이미지의 높이와 너비를 튜플로 반환.  h에는 이미지의 높이가, w에는 이미지의 너비가 저장됩니다.

map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)
#np.indices((h, w), dtype=np.float32):
#np.indices() 함수는 주어진 높이 h와 너비 w에 대한 좌표 매핑을 생성합니다.
#반환된 결과는 두 개의 배열로 구성됩니다: map1과 map2.
#dtype=np.float32는 배열 요소의 데이터 타입을 32비트 부동소수점으로 설정합니다.
#map2 = map2 + 10 * np.sin(map1 / 32):
#map1 배열은 x축 좌표를 나타내고, map2 배열은 y축 좌표를 나타냅니다.
#np.sin(map1 / 32)는 map1 배열의 각 요소에 대해 사인 함수를 계산합니다.
#이렇게 계산된 사인 값에 10을 곱한 후 map2 배열에 더합니다.
#이렇게 생성된 map1과 map2 배열은 이미지 변환에 사용되며, 좌표 매핑을 통해 이미지를 이동하거나 왜곡시킬 수 있습니다.
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)
print(map1[0:4])
print(map2[0:4])
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

#매핑의 주요 목적
#이미지 변환 (Image Transformation):
#좌표 매핑은 이미지를 변환하는 데 사용됩니다. 변환에는 크기 조정, 회전, 이동, 왜곡 등이 포함됩니다.

#부분 출력 (Region of Interest, ROI):

#ROI를 선택하고 해당 부분을 다른 이미지로 복사하거나 붙여넣을 때 좌표 매핑이 필요합니다.
#왜곡 보정 (Distortion Correction):
#카메라 렌즈 왜곡을 보정하기 위해 좌표 매핑을 사용합니다.
#렌즈 왜곡을 제거하고 이미지를 정확하게 표현하기 위해 좌표를 조정합니다.
#특수 효과 (Special Effects):
#좌표 매핑은 이미지에 특수 효과를 적용하는 데 사용됩니다.