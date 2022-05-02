import cv2
from cv2 import threshold
from matplotlib.pyplot import gray
import numpy as np

# reading image path
im1 = cv2.imread('./car.jpeg')
im2 = cv2.imread('./road.jpg')

car = cv2.resize(im1,(500,281))
road = cv2.resize(im2,(500,281))

# gray scale of car image
gray_image = cv2.cvtColor(car,cv2.COLOR_BGR2GRAY)

# threshold is the way of comparing the pixel values
# if pixel value is lower than threshold it is set to 0
ret, threshold = cv2.threshold(gray_image,150,255,cv2.THRESH_BINARY)
# inverse of mask
mask_inv = cv2.bitwise_not(threshold)


# combining the image
roadcom = cv2.bitwise_and(road,road, mask=threshold)
carcom = cv2.bitwise_and(car,car, mask=mask_inv)
finalbelnd = cv2.add(roadcom,carcom)

# showing image.
cv2.imshow("Masked",roadcom)
cv2.imshow("Masked inverse",carcom)
cv2.imshow("Blended",finalbelnd)


cv2.waitKey(0)
cv2.destroyAllWindows()

