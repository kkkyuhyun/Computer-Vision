import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1) #dx dy 행렬화 시켰다. 

mag = cv2.magnitude(dx, dy) #magnitude화
mag = np.clip(mag, 0, 255).astype(np.uint8) #clip으로 묶어주고 type도 실수형에서 정수형으로 바꿔주고 
#배열의 데이터 타입을 32비트 부동소수점에서 8비트 부호 없는 정수로 변환. 
# 이렇게 변환하면 픽셀 값이 정수로 표현되며, 이미지를 표시하거나 저장할 때 사용됩니다.

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255 #하얀색으로 
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)
#magnitude를 80으로 낮추면 더 많은 에지가 검출된다. 에지의 임계값을 낮추면 더 많은 임계값 형성, 높이게 된다면 아까보다 더 에지 검출 덜 된다. 
#그래디언트 검출. 
cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

#magnitude의 주 목적: 이미지 경계를 감지하고 픽셀 값의 크기를 조정하기 위함..