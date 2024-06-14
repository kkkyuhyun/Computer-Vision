import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 이미지 파일 경로
image_path = 'lenna.bmp'

# 컬러 이미지로 읽기
src = cv2.imread(image_path, cv2.IMREAD_COLOR)

if src is None:
    print('이미지 로드 실패')
    sys.exit()

# BGR 채널 분리
b, g, r = cv2.split(src)

# 히스토그램 계산
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# 히스토그램 그리기
plt.plot(hist_b, color='b', label='Blue')
plt.plot(hist_g, color='g', label='Green')
plt.plot(hist_r, color='r', label='Red')
plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# 컬러 이미지 출력
cv2.imshow('Color Image', src)
cv2.waitKey(0)
cv2.destroyAllWindows()
