import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 이미지를 흑백으로 읽어들입니다.
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)


# 이미지가 제대로 로드되었는지 확인합니다.
if src is None:
    print('Image load failed')
    sys.exit()

# 히스토그램을 계산합니다.
hist = cv2.calcHist([src], [0], None, [256], [0, 256])#calcHist(입력, 출력인덱스, 마스크연산, histsize, histrange)

# 원본 이미지를 화면에 표시합니다.
cv2.imshow('src', src)
cv2.waitKey(1)

# 히스토그램을 그래프로 표시합니다.
plt.plot(hist)
plt.show()