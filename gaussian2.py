# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

for sigma in range(1, 6): ###sigma값 1부터 5까지 순회시켜 노이즈를 제거한다. 시그마 값을 통해 부드러운 이미지를 만든다.
    # sigma 값을 이용하여 가우시간 필터링
    dst = cv2.GaussianBlur(src, (0, 0), sigma)

    desc = 'sigma = {}'.format(sigma)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA) #cv2.putText(추가이미지, 표시텍스트 내용, 텍스트 좌표, 텍스트 폰트, 텍스트 크기, 색, 텍스트 두께, 라인타입)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
