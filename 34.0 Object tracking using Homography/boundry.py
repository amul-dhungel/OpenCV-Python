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

    good_points = []
    for m, n in matches:
        # m is orignal image, which is downlaoded pic here
        # n is the trained image, which is video here
        if m.distance < 0.6 * n.distance:
            good_points.append(m)


    # Homography
    if len(good_points) > 10:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayFrame[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()

        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)

        homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)
        cv2.imshow("Homography", homography)
    
    else:
        cv2.imshow("Homography",grayFrame)

    # drawing keypoints on grayframe
    # grayFrame = cv2.drawKeypoints(grayFrame,kp_grayFrame,grayFrame)
    # cv2.imshow("Image",img)
    # cv2.imshow("Frame",img)

    key = cv2.waitKey(25)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



