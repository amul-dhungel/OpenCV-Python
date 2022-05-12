import cv2
import numpy as np

# reading of images object
img = cv2.imread("white.jpg",cv2.IMREAD_GRAYSCALE)

# using this function to detect horizontal or vertical
# functions.
sbolex = cv2.Sobel(img,cv2.CV_64F, 1, 0)
sboley = cv2.Sobel(img,cv2.CV_64F, 0, 1)
gaussian = cv2.GaussianBlur(img,(5,5),0)
# laplacian give us the better edge video result
# but still there will be much noises in the image
laplacian = cv2.Laplacian(img,cv2.CV_64F, ksize=5)

# this function provides the perfect edge without noise.
canny = cv2.Canny(gaussian,100,150)

# displaying of image in windows.
cv2.imshow("X image",sbolex)
cv2.imshow("Y image",sboley)
cv2.imshow("Laplace",laplacian)
cv2.imshow("Canny",canny)
cv2.imshow("Guassian",gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()