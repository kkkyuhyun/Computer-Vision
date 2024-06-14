import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

for ksize in (3, 5, 7): #ksize를 3,5,7로 순회하여 
    dst = cv2.blur(src, (ksize, ksize)) #3*3크기의 커널을 작은 크기로 블러링 빠르게 노이즈를 줄인다. 
    desc = 'Mean: {}x{}'.format(ksize, ksize) #desc에 블러링 크기에 표시하는 문자열을 생성한다. 
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                
#cv2.putText(이미지, 표시 텍스트,  텍스트 좌표, 텍스트 폰트 스타일, 텍스트 크기, 색상 텍스트 두께, 부드럽게 )
                1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
