import cv2
import numpy as np

# defining our video capture camera 
# 0 defines the frame rate which is fast
cap = cv2.VideoCapture(0)

# the video is runned continously, so while loop is used
while True:
    ret, frame = cap.read() 

    # to turn video into gray scale
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    
    cv2.imshow("gray_scale",gray_scale)
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)
    
    # if nothing is pressed , the loop goes on
    # which mans the video camera continus
    # if key 27 = "esc" is pressed, the video stops recording
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()