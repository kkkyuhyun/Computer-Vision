import sys
import numpy as np
import cv2


src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE) #color로 하면 각각의 계산량이 많아서 그레이스케일로 바꿔준다. 

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)  #150을 더 높이거나 낮추면 엣지로 인식하여 임계값이 더 분명하게 나타난다. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
