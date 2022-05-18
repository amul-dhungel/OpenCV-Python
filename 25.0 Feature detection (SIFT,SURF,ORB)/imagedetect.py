import cv2
import numpy as np 

# features are the part of information that describes the
# image, like corner, edges, pixels, colors. Suppose you have two
# books name "Halo", if you want to compare the two books in computer vision
# like 2 = 2, it is quite difficult, because computer vision is based on 
# pixel computation, and even a slight amount of light makes the two same book
# very much different. 

# reading the path of image
img = cv2.imread("book.jpg",cv2.IMREAD_GRAYSCALE)

#SIFT helps locate the local features in 
# an image, commonly known as the 'keypoints' of the image. These keypoints 
# are scale & rotation invariant that can be used for various computer 
# vision applications, like image matching, 
# object detection, scene detection, etc. 

sift = cv2.xfeatures2d.SIFT_create()

# its bit different but much faster
surf = cv2.xfeatures2d.SURF_create() 

keypoints, descriptiors = sift.detectAndCompute(img,None)

# drawing the keypoints on images of local features
img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("IMage",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

