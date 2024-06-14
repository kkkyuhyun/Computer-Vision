import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200], #x축을 200만큼, y축을 100만큼 이동시킨다. 
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
#src 원점에 있는 원본이미지를 어파인 변환행렬에 의하여 affine이동시킨 결과값만큼 나타낸 결과이다. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
