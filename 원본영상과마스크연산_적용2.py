import sys
import numpy as np
import cv2

# 원본 영상 불러오기
src = cv2.imread('bundang.jpg', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 얼굴 검출을 위한 분류기 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 얼굴 검출 수행
faces = face_cascade.detectMultiScale(src, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴이 검출되지 않으면 종료
if len(faces) == 0:
    print('Face detection failed!')
    sys.exit()

# 검출된 얼굴에 대한 마스크 생성
mask = np.zeros(src.shape[:2], dtype=np.uint8)
for (x, y, w, h) in faces:
    cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)  # 얼굴 부분을 흰색으로 채움

# BGR에서 YCrCb 색공간으로 변환
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# CrCb 살색 히스토그램 구하기
channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([src_ycrcb], channels, mask, [128, 128], ranges)
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상에 히스토그램 역투영 적용
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

# 역투영 결과를 마스크와 결합하여 얼굴 부분만 추출
face_only = cv2.bitwise_and(src, src, mask=mask)

# 결과 출력
cv2.imshow('src', src)
cv2.imshow('face_only', face_only)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
