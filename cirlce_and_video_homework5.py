import cv2

# ���콺 �ݹ� �Լ�
def draw_circle(event, x, y, flags, param):
    global oldx,oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame, (x, y), 100, (255, 0, 0))
        circles.append((x, y))

# ���� ĸó ��ü �ʱ�ȭ
cap = cv2.VideoCapture('video1.mp4')
# ���� ������ ���� ��ü �ʱ�ȭ
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

# Ŭ���� ��ġ�� ������ ����Ʈ
circles = []
cv2.namedWindow('video1')
cv2.setMouseCallback('video1', draw_circle)

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        continue

    # ����� ��ġ�� ���׶�� �׸���
    for center in circles:
        cv2.circle(frame, center, 100, (255, 0, 0))

    # �������� ȭ�鿡 ǥ��
    cv2.imshow('video1', frame)
    # �������� ���� ���Ͽ� ����
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ��� ��ü ����
cap.release()
out.release()
cv2.destroyAllWindows()
