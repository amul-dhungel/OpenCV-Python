import cv2
import numpy as np

# this corner detection is use to detected intersection of
# edges in real time or images

img = cv2.imread("corner.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# used to detect corners
corners = cv2.goodFeaturesToTrack(gray, 100,0.8,10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img,(x,y),5,(0,0,255), -1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()