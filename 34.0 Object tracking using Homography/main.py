'''
The homography has the ability to detect objects in videos
from the provided images of it.
'''

# this work in open-cv 4.0+ and opencv-contrib-python 4.0+
import cv2
from matplotlib.pyplot import gray 
import numpy as np 

img = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE)

cap = cv2.VideoCapture(0)

# Features detection
sift = cv2.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(img,None)


# drawing of keypoints on image
# img = cv2.drawKeypoints(img,kp_image,img)

# Features mathcing using of FLann
index_params = dict(algorithm=0,trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params,search_params)

while True:
    _, frame = cap.read()

    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # training image

    # detecting feautres in video 
    kp_grayFrame, desc_grayframe = sift.detectAndCompute(grayFrame,None)

    matches = flann.knnMatch(desc_image,desc_grayframe,k=2)

    good = []
    for m, n in matches:
        # m is orignal image, which is downlaoded pic here
        # n is the trained image, which is video here
        if m.distance < 0.8 * n.distance:
            good.append(m)


    # drawing of lines between two similar features of images or videos
    img3 = cv2.drawMatches(img,kp_image,grayFrame,kp_grayFrame,good,grayFrame)

    # drawing keypoints on grayframe
    # grayFrame = cv2.drawKeypoints(grayFrame,kp_grayFrame,grayFrame)
    # cv2.imshow("Image",img)
    cv2.imshow("Frame",img3)

    key = cv2.waitKey(25)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



