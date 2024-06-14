import matplotlib.pyplot as plt
import cv2


imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('on')
plt.imshow(imgRGB)
plt.show()

imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

plt.subplot(211), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(212), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()

