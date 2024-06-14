import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
#검은색 관계가 잘 보일 수 있도록 . 경계 엣지들이 소벨 미분이 되어 검출될 수 있게 출력
#src: 입력 이미지입니다. 경계를 감지할 이미지를 지정합니다.
#-1: 출력 이미지의 데이터 타입입니다. -1은 입력 이미지와 동일한 데이터 타입을 사용하도록 지정합니다.
#1과 0: 소벨 필터의 x축 및 y축 방향으로의 차분 차수입니다. 1은 x축 방향으로 1차 미분을 수행하고, 0은 y축 방향으로 미분을 수행하지 않음을 의미합니다.
#delta=128: 경계 감지 결과에 추가적인 값을 더합니다. 이는 경계를 더 선명하게 표시하기 위해 사용됩니다.
dx = cv2.Sobel(src, -1, 1, 0) #delta를 지웠을 때, 경계를 덜 선명하게 한다. 
dy = cv2.Sobel(src, -1, 0, 1, delta=128) #검은색 관계가 잘 보일 수 있도록 . 경계 엣지들이 소벨 미분이 되어 검출될 수 있게 출력
#방향 dx는 x축방향으로 경계를 감지하고, dy는 y축 방향으로 경계를 감지한다
#미분 방향dx는 x축 방향으로 미분을 수행하고, dy는 y축 방향으로 미분을 수행한다
#결과 dx는 x축 방향으로 경계를 감지하고 dy는 y축 방향으로 경계를 감지한다. 
dy = cv2.Sobel(src, -1, 1, 0) #delta를 지웠을 때

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
