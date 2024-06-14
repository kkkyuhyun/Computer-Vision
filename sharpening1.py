import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE) #소스이미지

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2) #부드러워지기 위해서 블러처리를 한다. (★알고리즘 기억하기!)
dst1 = cv2.subtract(src,blr) #subtract을 통하여 원본이미지 - 블러처리이미지 = 검은색 배경들은 CV07 p.28 함수에서 올곧(좌표상)은 부분 제외 출력된 것. 
dst2 = cv2.addWeighted(src,1, blr,-1, 128)#src, 1첫번째 이미지 가중치, blr 두번째 입력 이미지 가우시안 블러링, -1 두번째 이미지 가중치 , 128 결과 이미지 추가 더한 값 밝기 조절
dst3 = cv2.addWeighted(src,2, blr,-1, 0) #출력결과 윤곽선이 더 뚜렷해짐을 확인할 수 있다. addweighted에 0을 출력하면 맨 처음과 비슷한 sharp가 출력된다. 
dst4 = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)#출력결과 윤곽선이 더 뚜렷해짐을 확인할 수 있다. # src 앞에 배수가 더 강해질 수록 하얀색이 더 강조된다. 


cv2.imshow('src', src)
cv2.imshow('blr',blr)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.waitKey()

cv2.destroyAllWindows()
