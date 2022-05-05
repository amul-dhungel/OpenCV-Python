import cv2
from cv2 import rotate
import numpy as np

# reading images
img = cv2.imread('red_panda.jpg')
rows, cols, ch = img.shape

print

# scaled image by managing x and y length
scaled = cv2.resize(img,None,fx=2,fy=1/2)

# translated image
matrix = np.float32([[1,0,-100],[0,1,-30]])
translated = cv2.warpAffine(img,matrix,(cols,rows))

# rotated image
matrix_r = cv2.getRotationMatrix2D((cols/2, rows/2) , 90,0.5)
rotated_img = cv2.warpAffine(img,matrix_r,(cols,rows))

# displaying image
cv2.imshow("Scaled",scaled)
cv2.imshow("Trans",translated)
cv2.imshow("Rotate",rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()