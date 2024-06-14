import cv2

# 마우스 콜백 함수
def draw_circle(event, x, y, flags, param):
    global oldx,oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame, (x, y), 100, (255, 0, 0))
        circles.append((x, y))

# 비디오 캡처 객체 초기화
cap = cv2.VideoCapture('video1.mp4')
# 비디오 저장을 위한 객체 초기화
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

# 클릭된 위치를 저장할 리스트
circles = []
cv2.namedWindow('video1')
cv2.setMouseCallback('video1', draw_circle)

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        continue

    # 저장된 위치에 동그라미 그리기
    for center in circles:
        cv2.circle(frame, center, 100, (255, 0, 0))

    # 프레임을 화면에 표시
    cv2.imshow('video1', frame)
    # 프레임을 비디오 파일에 쓰기
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 모든 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()
