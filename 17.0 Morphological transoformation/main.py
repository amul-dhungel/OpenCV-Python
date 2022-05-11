import cv2
import numpy as np

# morphological transformation is used to remove 
# noise from an image.

img = cv2.imread("balls.jpg",cv2.IMREAD_GRAYSCALE)

# creating threshold 
_, mask = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)

# as we can find there are noises,errors in the image
# to remove it we need to fill the noises
kernel = np.ones((5,5),np.uint8)
# The function dilates the source image using the specified 
# structuring element that determines the shape 
# of a pixel neighborhood over which the maximum is taken
dilate = cv2.dilate(mask,kernel)

# The function erodes the source image using 
# the specified structuring element that determines 
# the shape of a pixel  neighborhood over 
# which the minimum is taken

# the more we iteration, the more the function performs
# erosion on previous eroded images and it gets improved.
erosion = cv2.erode(mask,kernel,iterations=3)



cv2.imshow("Orange",img)
cv2.imshow("Mask",mask)
cv2.imshow("DIlation",dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()
