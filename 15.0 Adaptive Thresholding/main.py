import cv2
from cv2 import threshold
import numpy as np

# reading of image path
img = cv2.imread("book_page.jpg")

# converting the image into threshold layout
_, threshold = cv2.threshold(img,110,255,cv2.THRESH_BINARY)

#converting the image in gray scale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

mean_c = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,12)
gaus = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,12)


# showing of images
cv2.imshow("Frame",img)
cv2.imshow("Binary Threshold",threshold)
cv2.imshow("Thresh",mean_c)
cv2.imshow("Gaussian",gaus)

cv2.waitKey(0)
cv2.destroyAllWindows() 