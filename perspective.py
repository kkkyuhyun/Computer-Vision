import sys
import numpy as np
import cv2


src = cv2.imread('tag.png')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[85, 490], [618, 365], [809, 623], [229, 813]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

#투시변환: 원근감을 고려하여 이미지를 변환하는 기법, 원근 효과 보정
#투시변환: 3*3 행렬로 4개의 입력 점과 해당 점들 매핑 4개 출력 점 사용
#어파인변환: 이미지 크기 조정 이동 기울임 변환 원근 효과 고려X 평행 선 유지 이미지 변환
#어파인변환:2*3행렬로 3개의 입력 점과 해당 점들 매핑 3개 출력 점 사용
# > 투시변환은 원근 효과를 보정하고, 어파인변환은 평행 선 유지 이미지 변환 


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
