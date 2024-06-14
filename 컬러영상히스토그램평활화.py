import sys
import numpy as np
import cv2

# 이미지를 불러옵니다.
src = cv2.imread('field.bmp')

# 이미지가 제대로 불러와졌는지 확인합니다.
if src is None:
    print("failed to load image")
    sys.exit()

# BGR에서 YCrCb 색공간으로 변환합니다.
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# YCrCb 채널을 분리합니다.
ycrcb_planes = cv2.split(src_ycrcb)

# Y 채널의 히스토그램을 균등화합니다.
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

# 균등화된 채널을 다시 합칩니다.
dst_ycrcb = cv2.merge(ycrcb_planes)

# YCrCb에서 BGR 색공간으로 변환합니다.
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR) 

# 원본 이미지와 결과 이미지를 보여줍니다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()  # 모든 창을 닫습니다.
