import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src=cv2.imread('lenna.bmp')
colors=['b','g','r']
bgr_planes = cv2.split(src) #ä�� �и� 

if src is None:
    print('Image Load Failed')
    sys.exit()
    
colors=['b','g','r']
bgr_planes = cv2.split(src)
for(p,c) in zip(bgr_planes,colors): #�� �κ��� bgr_planes ����Ʈ�� colors ����Ʈ�� ���ÿ� ��ȸ�ϴ� ������ �����մϴ�. 
    #bgr_planes�� �̹����� BGR ä���� �и��� ���̰�, colors�� �� ä�ο� �ش��ϴ� ������ ��Ÿ���ϴ�.
    hist=cv2. calcHist([p],[0], None, [256], [0,256])
    plt.plot(hist,color=c)#plt,plot(������ ����Ʈ, �׷��� C ���� ����)
cv2.imshow('src',src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()