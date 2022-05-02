import cv2
from cv2 import threshold
from matplotlib.pyplot import gray
import numpy as np

# reading image path
im1 = cv2.imread('./car.jpeg')
im2 = cv2.imread('./road.jpg')

# gray scale of car image
gray_image = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)

# threshold is the way of comparing the pixel values
# if pixel value is lower than threshold it is set to 0
ret, threshold = cv2.threshold(gray_image,150,255,cv2.THRESH_BINARY)

# summing the original image and threshold
sum = cv2.add(im1,im1,mask=threshold)
cv2.imshow("TH",threshold)
cv2.imshow("GRay",sum)

cv2.waitKey(0)
cv2.destroyAllWindows()

