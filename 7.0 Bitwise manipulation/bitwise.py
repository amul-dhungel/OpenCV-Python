import cv2
from cv2 import bitwise_and
import numpy as np

# reading image path
im1 = cv2.imread('./drawing_1.png')
im2 = cv2.imread('./drawing_2.png')

# resizing shape of image 
img1 = cv2.resize(im1,(500,281))
img2 = cv2.resize(im2,(500,281))

# bitwise manipulation
# bitwase simply peform the computation on pixel values
# when 0 = white, 1 = black is multiplied (and), the result will
# 0 x 1 = 0, 0 x 0 = 0, 1 , 1 x 1 = 1
bit_and = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_xor = cv2.bitwise_xor(img1,img2)
bit_not = cv2.bitwise_not(img1,img2)

# displaying image
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not",bit_not)


cv2.waitKey(0)
cv2.destroyAllWindows()