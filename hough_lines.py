import sys
import numpy as np
import cv2


src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150) #canny로 엣지화 시켜줌

lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160, #허프 확률 입력 
                        minLineLength=50, maxLineGap=5)
#허프라인 edge이미지, 각도 해상도 라디안 단위로 설정하고, 허프 확률 입력값, 검출 직선의 최소 길이, 검출 직선의 최대길이

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):             # 검출된 직선 정보를 이용해서 dst이미지를 그린다.
        pt1 = (lines[i][0][0], lines[i][0][1])  # i번째 직선 첫번째의 x좌표, i번째 직선의 첫번째 y좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # i번째 직선 두번째의 x좌표, i번째 직선의 두번째 y좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA) #선 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
