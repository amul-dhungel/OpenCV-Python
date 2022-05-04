import cv2
import numpy as np


def nothing(x):
    pass
# taking priviledges from video camera
cap = cv2.VideoCapture(0)

# adding trackbar,slider in windows in the sameframe
cv2.namedWindow("Frame")
cv2.createTrackbar("test","Frame",50,500,nothing)
cv2.createTrackbar("color/gray","Frame",0,1,nothing)

while True:
    # reading the frame from the camera
    _, frameimage = cap.read()
    
    number = cv2.getTrackbarPos("test","Frame")
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frameimage,text = str(number),org=(50,150),fontFace=font,fontScale=4,color = (0,0,255))

    # for color chaing while slider moves
    colorchange = cv2.getTrackbarPos("color/gray","Frame")
    if colorchange == 0:
        pass
    else:
        frameimage = cv2.cvtColor(frameimage,cv2.COLOR_BGR2GRAY)

    # opening camera in the form of continous frame
    cv2.imshow("Frame",frameimage)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()