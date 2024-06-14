import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
dst2=cv2.flip(src,-1,dst=None) 
#flip이라는 함수를 이용하여 상하좌우 대칭을 만들 수 있다. 양수일때 좌우, 0일때 상하, 음수일때 좌우상하 
dst3=cv2.flip(src,1,dst=None)
dst4=cv2.flip(src,0,dst=None)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()
cv2.destroyAllWindows()