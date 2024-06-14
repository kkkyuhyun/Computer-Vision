import numpy as np
import cv2

def on_change(pos):
    #print(pos)
    level=pos*16 #0부터 16
    if level>255:
        level=255
        
    img[:,:]=level
    cv2.imshow('image',img)
img = np.zeros((480,640),np.uint8)
cv2. namedWindow('image')
cv2. createTrackbar('level1','image',0,16,on_change) #창이 먼저 생성된다는 게 중요하다. 

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
