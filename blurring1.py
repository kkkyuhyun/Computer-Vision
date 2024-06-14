import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

kernel = np.ones((3, 3), dtype=np.float64) / 9. #3*3크기의 모든 요소를 9로 나누어 평균을 계산한다 
dst = cv2.filter2D(src, -1, kernel) #2D필터링 수행하는 코드로 Src에 커널을 적용하여 결과를 생성한다. (src, depth, kernel)
dst = cv2.blur(src, (3, 3)) #src이미지를 3*3크기 블러링한다. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
