import numpy as np
import cv2
img = np.full((400,400,3),255,np.uint8)

cv2.line(img,(50,165),(250,165),(0,0,255),5)
cv2.circle(img,(150,230),80,(0,0,0),3,cv2.LINE_AA)
cv2.circle(img, (150,100),50,(0,0,0),3, cv2.LINE_AA)

cv2.imshow('img1',img)
cv2.waitKey()
cv2.destroyAllWindows()


