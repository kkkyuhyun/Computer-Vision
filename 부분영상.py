import numpy as np
import cv2

# Read the image
img1 = cv2.imread('HappyFish.jpg')

# Create sub-images
img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()

# Fill img2 with zeros (black)
img2.fill(0)

# Display the images
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

# Wait for a key press and then destroy all windows
cv2.waitKey()
cv2.destroyAllWindows()
