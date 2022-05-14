import cv2
import numpy as np

# template matching is technique of matching sections of one image
# to other images  to check the similarity.

cap = cv2.VideoCapture(0)

# cropped picture of an object, that is to be detected
# in the video
template = cv2.imread('box.jpg',cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

while True:
    # recording video continously
    _, frame = cap.read()

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(gray_frame,template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.5)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt, (pt[0] + w, pt[1] + h), (0,255,0),3)

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()