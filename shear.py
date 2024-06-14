import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0], #x���� 0.5�� Ȯ��, y���� Ȯ�� X 
                [0, 1, 0]], dtype=np.float32)
# x��: �̵��Ϸ��� [ , , 0.5]0.5��ŭ �̵��̾�� �ϰ� [ , 0.5 ,  ]�� 0.5�� Ȯ�븦 ���Ѵ�. 
# y��: [0,1,2] x�� ũ�� �̵� ���� y������ 2��ŭ �̵��ϴ� ��ȯ, [0,1,-2] �� y�� �������� Ȯ���ϰڴٴ� �� 
#�������ڸ� x�� �������� Ȯ��� ����° ���� 0���� ũ�� �ǰ�, 0���� ������ y�� �������� Ȯ��
#�׸��� �̵�: x�� �������� �̵��ϴ� ���� �ι��� ���� ���� ���� �̵� ��ȯ�� ��Ÿ����. 


#���� ��ȯ�� ũ�� ����, ȸ��, �̵� ���� ��ȯ�� �����ϸ�, ���� ��ȯ�� �߰����� ���⸦ �����ϴ� ��ȯ�Դϴ�
h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h)) 
#���̴� ���� �̹����� �����ϸ�, �ʺ�� ���� �ʺ� ������ 0.5�踦 ���� ���Դϴ�.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

#������ ���� ��ȯ ����
#import sys import cv2 import numpy as np
#if src is None:
#print("failed to load image")
#sys.exit()
#rad=45*math.pi/180 
#aff=np.array([[math.cos(rad),math.sin(rad),0], [-math.sin(rad),math.cos(rad),0]], dtype=np.float32)
#2*3 ��� �⺻���� �Ǽ��̴�. warpAffine��ķ� �̵�, ���� 2*3��� ������ �������� ��ȯ��Ų��. 
#dst=cv2.warpAffine('dst',dst)
#cv2.imshow('src',src) cv2.waitKey() cv2.destroyAllWindows()

