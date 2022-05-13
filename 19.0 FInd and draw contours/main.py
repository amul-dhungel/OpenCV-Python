import cv2
import numpy as np
 
#defining video capture
cap = cv2.VideoCapture(0)

while True:
    # recording video continously
    _, frame = cap.read()

    # blurring to remove background
    blurred_frame = cv2.GaussianBlur(frame,(5,5),0)
    # managing color
    hsv = cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)

    # defining range of colors
    lower_blue = np.array([30,86,0])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(frame,contours, -1, (0,255,0),3)

    # displaying video
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
