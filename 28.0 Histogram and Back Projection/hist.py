import cv2 
import numpy as np
from matplotlib import pyplot as plt 

"""" back projection is the way of calculating the histogram
of the image, and then use it as feature to detect similar feature
in the whole image"""

original_img = cv2.imread("goalkeeper.jpg")
# convert image into hsv format
hsv_original = cv2.cvtColor(original_img,cv2.COLOR_BGR2HSV)

roi_image = cv2.imread("pitch_ground.jpg")
# convert image into hsv format
hsv_roi = cv2.cvtColor(roi_image,cv2.COLOR_BGR2HSV)

# compute the histogram of sample ROI image for evaluating
# with larger image in further process
roi_hist = cv2.calcHist([hsv_roi],[0,1],None,[180,256],[0,180,0,256])

# the below function, compares the histogram of 2 images, and
# based on the close evaluation, it will change into gray scale bacgkround
# that means, similar hsv values will be white remaining all black.
mask = cv2.calcBackProject([hsv_original],[0,1],roi_hist,[0,180,0,256],1)

# Filtering for removing the noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
masknoise = cv2.filter2D(mask,-1,kernel)
_, maskthres = cv2.threshold(masknoise,50,255,cv2.THRESH_BINARY)

# blending of mask image with original image
maskmerge = cv2.merge((maskthres,maskthres,maskthres))
result = cv2.bitwise_and(original_img,maskmerge)


cv2.imshow("Original Image", original_img)
cv2.imshow("ROI",result)
cv2.imshow("Mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(roi_hist)
# plt.show()