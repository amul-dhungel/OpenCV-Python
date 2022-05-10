import cv2
import numpy as np

img = cv2.imread('balloons_noisy.png')

# bluring of images, it takes the 5 by 5 pixel size
# of an image, and takes the average of every pixel 
# the below are the kernels or filters.
averaging = cv2.blur(img,(5,5))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,5,75,75)

cv2.imshow("Original Image",img)
cv2.imshow("Blur image",averaging)
cv2.imshow("Guassian image",gaussian)
cv2.imshow("Median image",median)
cv2.imshow("Bilateral image",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()