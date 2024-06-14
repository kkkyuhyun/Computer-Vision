import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0], #x축을 0.5배 확대, y축은 확대 X 
                [0, 1, 0]], dtype=np.float32)
# x축: 이동하려면 [ , , 0.5]0.5만큼 이동이어야 하고 [ , 0.5 ,  ]는 0.5배 확대를 뜻한다. 
# y축: [0,1,2] x축 크기 이동 없이 y축으로 2만큼 이동하는 변환, [0,1,-2] 는 y축 방향으로 확대하겠다는 뜻 
#정리하자면 x축 방향으로 확대는 세번째 값이 0보다 크면 되고, 0보다 작으면 y축 방향으로 확대
#그리고 이동: x축 방향으로 이동하는 것은 두번재 값의 수에 따라 이동 변환을 나타낸다. 


#아핀 변환은 크기 조정, 회전, 이동 등의 변환을 수행하며, 전단 변환은 추가적인 기울기를 적용하는 변환입니다
h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h)) 
#높이는 원래 이미지와 동일하며, 너비는 원래 너비에 높이의 0.5배를 더한 값입니다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

#영상의 전단 변환 예제
#import sys import cv2 import numpy as np
#if src is None:
#print("failed to load image")
#sys.exit()
#rad=45*math.pi/180 
#aff=np.array([[math.cos(rad),math.sin(rad),0], [-math.sin(rad),math.cos(rad),0]], dtype=np.float32)
#2*3 행렬 기본값은 실수이다. warpAffine행렬로 이동, 전단 2*3행렬 영상은 기하학적 변환시킨다. 
#dst=cv2.warpAffine('dst',dst)
#cv2.imshow('src',src) cv2.waitKey() cv2.destroyAllWindows()

