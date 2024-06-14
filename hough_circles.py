import sys
import numpy as np
import cv2


# ?��?�� ?��미�?? 불러?���?
src = cv2.imread('dial.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) #�Է°� gray 
blr = cv2.GaussianBlur(gray, (0, 0), 1.0) #���� �� �ϵ��� gaussian blur , ��� ����, ���� ���� �̹��� �� �ε巴��


def on_trackbar(pos): #Ʈ���� ���� �Ӱ谪 ������ �߿伺
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    #Ʈ���ٸ� ����ϴ� ������ �Ű������� �ǽð����� �����ϱ� �����̴�. 

    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
# blr: �̹������� ���� ������ �� ���Ǵ� ��ó���� �̹����Դϴ�. ���� �̹����� ������� ��ȯ�ϰų� ����� ������ �Ŀ� ���˴ϴ�.
#cv2.HOUGH_GRADIENT: ���� ��ȯ �˰����� ����� �����մϴ�. ���⼭�� �׶���Ʈ ����� ����մϴ�.
#1: �ȼ� �ػ� �����Դϴ�. 1�� ���� �̹����� ������ �ػ󵵸� ����Ѵٴ� �ǹ��Դϴ�.
#50: �� ���⿡ ���Ǵ� ���� ��ȯ�� ������ �迭 ũ���Դϴ�.
#param1: ���� ��ȯ �˰����� ù ��° �Ű�������, ���������� ���Ǵ� ���Դϴ�.
#param2: ���� ��ȯ �˰����� �� ��° �Ű�������, �� ������ ���� �Ӱ谪�Դϴ�.
#minRadius: ������ ���� �ּ� �������Դϴ�.
#maxRadius: ������ ���� �ִ� �������Դϴ�.
# param1, param2, minRadius, maxRadius ���� �����Ͽ� �� ������ ������ ����
    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = np.uint16(circles[0][i]) #i��° ���� �߽���ǥ�� �������� ��� �ִ� �迭.
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


# ?��?���? ?��?��
cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()

cv2.destroyAllWindows()

#Ʈ���� ����
#Ʈ���ٸ� ����� �� getTrackbarPos�� createTrackbar, setTrackbarPos �Լ��� �Բ� ����ϴ� ������ ������ �����ϴ�:
#Ʈ���� ���� (createTrackbar):
#�� �Լ��� ����Ͽ� Ʈ���ٸ� ȭ�鿡 ǥ���ϰ� ����ڰ� ���� ������ �� �ֵ��� �մϴ�.
#Ʈ���ٸ� ������ ���� �ʱⰪ, �ּҰ�, �ִ밪 ���� �����մϴ�.
#Ʈ���� �� �б� (getTrackbarPos):
# Ʈ������ ���� ���� �о�ɴϴ�. �� �Լ��� ����Ͽ� ����ڰ� Ʈ���ٸ� �����Ͽ� ������ ���� �����ɴϴ�.
#�� ���� ������ �����Ͽ� �ٸ� �κп��� ����� �� �ֽ��ϴ�.
#Ʈ���� �� ���� (setTrackbarPos):
#setTrackbarPos �Լ��� Ʈ������ ���� �����մϴ�. �� �Լ��� ����Ͽ� Ʈ������ ���� ������ �� �ֽ��ϴ�.
