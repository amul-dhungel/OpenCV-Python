# the two same books have different features because of
# sensitive computation of pixels based

import cv2
import numpy as np 


# reading the path of image
img = cv2.imread("book.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("holding.jpg",cv2.IMREAD_GRAYSCALE)

#OBR detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# here descriptor is an array of number, and these numbers 
# are responsible for features representation. 
# To compare features, we cannot compare pixels by pixels because
# of lightning and rotation. 

# Brute force matching
# it is going to match first and second descriptor to both images
# if you don't put crosscheck, it going to check first descriptor
# with all other descriptors in second image, with crosscheck we
# only perform the best match.
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

for m in matches:
    # the lesser the distance, the more the features
    # are similar between two images.
    print(m.distance)
    
matching_result = cv2.drawMatches(img,kp1,img2,kp2,matches[:20],None)
# for d in des1:
#     print(d)

cv2.imshow("IMG1",img)
cv2.imshow("IMG2",img2)
cv2.imshow("Matches",matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

