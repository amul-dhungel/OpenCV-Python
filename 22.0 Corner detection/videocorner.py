import cv2
import numpy as np


def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Corners")
cv2.createTrackbar("quality","Corners",1,100,nothing)

while True:
    ret, frame = cap.read()

    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    quality = cv2.getTrackbarPos("quality", "Corners")
    quality = quality /100 if quality > 0 else 0.01
    # used to detect corners
    corners = cv2.goodFeaturesToTrack(grayvideo, 100,quality,100)
    
    if corners is not None:
        for corner in corners:
            corners = np.int0(corners)
            # extracting the x,y points of corners
            x, y = corner.ravel()
            # plotting circle on those points
            cv2.circle(frame,(x,y),5,(0,0,255), -1)

    cv2.imshow("Corners",frame)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()