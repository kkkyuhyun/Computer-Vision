import sys
import numpy as np
import cv2

# 콜백 함수
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
        # 클릭한 위치에 파란색 원을 그립니다.
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)  # -1은 원 내부를 채우는 것을 의미합니다.
        # 원의 중심에서 수평으로 선을 그립니다.
        cv2.line(img, (x - 25, y), (x + 25, y), (0, 0, 255), 2)
        # 원의 중심에서 수직으로 선을 그립니다.
        cv2.line(img, (x, y - 25), (x, y + 25), (0, 0, 255), 2)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('image', img)

# 이미지를 생성합니다.
img = np.ones((480, 640, 3), dtype=np.uint8) * 255

# 윈도우를 생성하고 콜백 함수를 설정합니다.
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse)

# 이미지를 표시합니다.
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
