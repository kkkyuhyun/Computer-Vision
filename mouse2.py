import sys 
import numpy as np
import cv2

# �ݹ� �Լ�
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(param, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', param)
            oldx, oldy = x, y

# �̹����� �����մϴ�.
img = np.ones((480, 640, 3), dtype=np.uint8) * 255

# �����츦 �����ϰ� �ݹ� �Լ��� �����մϴ�.
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

# �̹����� ǥ���մϴ�.
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
