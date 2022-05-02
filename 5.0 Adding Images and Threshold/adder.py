import cv2
import numpy as np


# reading image path
im1 = cv2.imread('./car.jpeg')
im2 = cv2.imread('./road.jpg')

# resize image, because for mergin two images,
# the array which is height & width should be same.
# it basically adds all the pixel, so the matrix shape
# should be same or equal.
car = cv2.resize(im1,(500,281))
road = cv2.resize(im2,(500,281))


# merging of two images in one
# here, the function, add two pixel of two different images
# and displays the final combination images
sums = cv2.add(car,road)

weighted = cv2.addWeighted(car,1,road,0.3,0)

# showing of images in windows
# cv2.imshow("im1",im1)
# cv2.imshow("im2",im2)
cv2.imshow("sum",weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()