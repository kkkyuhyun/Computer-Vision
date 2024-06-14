import sys
import numpy as np
import cv2


src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE) #color�� �ϸ� ������ ��귮�� ���Ƽ� �׷��̽����Ϸ� �ٲ��ش�. 

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)  #150�� �� ���̰ų� ���߸� ������ �ν��Ͽ� �Ӱ谪�� �� �и��ϰ� ��Ÿ����. 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
