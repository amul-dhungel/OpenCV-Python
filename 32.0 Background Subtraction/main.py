import cv2
from cv2 import threshold 
import numpy as np 

cap = cv2.VideoCapture("highway.mp4")

# capturing of first frame
_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
# making the gray foramt to remove background blury
first_gray = cv2.GaussianBlur(first_gray, (5,5),0)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # again making the video little blurry
    gray_frame = cv2.GaussianBlur(gray_frame,(5,5),0)

    # subtracting of first frame from pixels from the video
    difference = cv2.absdiff(first_gray,gray_frame)

    # managing threshold to make it more black or white
    ret, threshold = cv2.threshold(difference,25,255,cv2.THRESH_BINARY)

    cv2.imshow("Frame",threshold)

    key = cv2.waitKey(25)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()