import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src=cv2.imread('lenna.bmp')
colors=['b','g','r']
bgr_planes = cv2.split(src) #채널 분리 

if src is None:
    print('Image Load Failed')
    sys.exit()
    
colors=['b','g','r']
bgr_planes = cv2.split(src)
for(p,c) in zip(bgr_planes,colors): #이 부분은 bgr_planes 리스트와 colors 리스트를 동시에 순회하는 루프를 생성합니다. 
    #bgr_planes는 이미지의 BGR 채널을 분리한 것이고, colors는 각 채널에 해당하는 색상을 나타냅니다.
    hist=cv2. calcHist([p],[0], None, [256], [0,256])
    plt.plot(hist,color=c)#plt,plot(데이터 포인트, 그래프 C 색상 지정)
cv2.imshow('src',src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()