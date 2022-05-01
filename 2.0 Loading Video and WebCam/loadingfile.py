import cv2
import numpy as np


# to load video from file dataset
cap = cv2.VideoCapture("./video.mp4")

while True:
    ret, frame = cap.read()

    gray_scale = gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # flipping the video
    # frame2 = cv2.flip(frame,2)

    # displaying video/image function
    # cv2.imshow("frame flip",frame2)
    cv2.imshow("frame",gray_scale)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
    