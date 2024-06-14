import sys
import numpy as np
import cv2


# ?엯?젰 ?씠誘몄?? 遺덈윭?삤湲?
src = cv2.imread('dial.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) #입력값 gray 
blr = cv2.GaussianBlur(gray, (0, 0), 1.0) #검출 잘 하도록 gaussian blur , 경계 감지, 잡음 제거 이미지 더 부드럽게


def on_trackbar(pos): #트랙바 설정 임계값 설정의 중요성
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    #트랙바를 사용하는 이유는 매개변수를 실시간으로 조정하기 위함이다. 

    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
# blr: 이미지에서 원을 검출할 때 사용되는 전처리된 이미지입니다. 보통 이미지를 흑백으로 변환하거나 노이즈를 제거한 후에 사용됩니다.
#cv2.HOUGH_GRADIENT: 허프 변환 알고리즘의 방법을 지정합니다. 여기서는 그라디언트 방법을 사용합니다.
#1: 픽셀 해상도 비율입니다. 1은 원본 이미지와 동일한 해상도를 사용한다는 의미입니다.
#50: 원 검출에 사용되는 허프 변환의 누적자 배열 크기입니다.
#param1: 허프 변환 알고리즘의 첫 번째 매개변수로, 내부적으로 사용되는 값입니다.
#param2: 허프 변환 알고리즘의 두 번째 매개변수로, 원 검출을 위한 임계값입니다.
#minRadius: 검출할 원의 최소 반지름입니다.
#maxRadius: 검출할 원의 최대 반지름입니다.
# param1, param2, minRadius, maxRadius 값을 조정하여 원 검출의 성능을 조절
    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = np.uint16(circles[0][i]) #i번째 원의 중심좌표와 반지름을 담고 있는 배열.
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


# ?듃?옓諛? ?깮?꽦
cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()

cv2.destroyAllWindows()

#트랙바 설명
#트랙바를 사용할 때 getTrackbarPos와 createTrackbar, setTrackbarPos 함수를 함께 사용하는 이유는 다음과 같습니다:
#트랙바 생성 (createTrackbar):
#이 함수를 사용하여 트랙바를 화면에 표시하고 사용자가 값을 조정할 수 있도록 합니다.
#트랙바를 생성할 때는 초기값, 최소값, 최대값 등을 설정합니다.
#트랙바 값 읽기 (getTrackbarPos):
# 트랙바의 현재 값을 읽어옵니다. 이 함수를 사용하여 사용자가 트랙바를 조작하여 설정한 값을 가져옵니다.
#이 값을 변수에 저장하여 다른 부분에서 사용할 수 있습니다.
#트랙바 값 설정 (setTrackbarPos):
#setTrackbarPos 함수는 트랙바의 값을 설정합니다. 이 함수를 사용하여 트랙바의 값을 변경할 수 있습니다.
