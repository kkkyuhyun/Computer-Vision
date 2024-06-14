import sys
import numpy as np
import cv2

# �ݹ� �Լ�
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
        # Ŭ���� ��ġ�� �Ķ��� ���� �׸��ϴ�.
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)  # -1�� �� ���θ� ä��� ���� �ǹ��մϴ�.
        # ���� �߽ɿ��� �������� ���� �׸��ϴ�.
        cv2.line(img, (x - 25, y), (x + 25, y), (0, 0, 255), 2)
        # ���� �߽ɿ��� �������� ���� �׸��ϴ�.
        cv2.line(img, (x, y - 25), (x, y + 25), (0, 0, 255), 2)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('image', img)

# �̹����� �����մϴ�.
img = np.ones((480, 640, 3), dtype=np.uint8) * 255

# �����츦 �����ϰ� �ݹ� �Լ��� �����մϴ�.
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse)

# �̹����� ǥ���մϴ�.
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
