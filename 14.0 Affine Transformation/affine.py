# An affine transformation is any transformation that preserves collinearity 
# (i.e., all points lying on a line initially still lie on a line after
#  transformation) and ratios of distances (e.g., the midpoint of a line
#   segment remains the midpoint after transformation).

import cv2
import numpy as np

img = cv2.imread('grid.jpg')
rows, cols , ch  = img.shape

# drawing of circle on image
cv2.circle(img,(83,90),5,(0,0,255),-1)
cv2.circle(img,(450,90),5,(0,0,255),-1)
cv2.circle(img,(83,472),5,(0,0,255),-1)

# points
pts1 = np.float32([[83,90],[447,90],[83,472]])
pts2 = np.float32([[30,90],[447,90],[83,472]])

# applying affine transformation
matrix = cv2.getAffineTransform(pts1,pts2)
print(matrix)
result = cv2.warpAffine(img,matrix,(cols,rows))

# always display the image after processing 
# because python is an interpreter 
cv2.imshow("Image",img)
cv2.imshow("Affine transformation",result)

cv2.waitKey(0)
cv2.destroyAllWindows()