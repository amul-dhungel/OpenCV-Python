import cv2
import numpy as np

img = cv2.imread("hands.jpg")

# Gaussian Pyramid
# The Gaussian pyramid is a technique in image processing 
# that breaks down an image size/resolution into successively 
# smaller groups of pixels to blur it.
layer = img.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    # cv2.imshow(str(i),layer)


# laplacian pyramid
# breaking down image into smaller piece, and again
# extending it into bigger piece causes decrease in
# original resolution.
layer = gaussian_pyramid[5]
laplacian_pyramid = [layer]
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i - 1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)
    cv2.imshow(str(i), laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()