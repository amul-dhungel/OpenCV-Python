from re import X
import cv2 
import numpy as np

img = cv2.imread("teapot.jpg")

x = 373
y = 160 
width = 560 - x 
height = 300 - y 


# cropping of image
roi = img[160:300,373:560] 

# converting of hsv to above image for calculating the hsv value
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

# calculating the histogram of cropped image, so that
# in further, its histogram value and the section of that object
# hsv value in video is evaluated to track
roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180])

cap = cv2.VideoCapture(0)

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

while True:
    _, frame = cap.read()

    # covnerting of video into hsv format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # evaluating the hsv format with the cropped image value for the evaluation
    mask = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

    # tracking object for rotation unlike mean-shift which cannot rotate, it can rotate.
    ret, track_window = cv2.CamShift(mask, (x,y,width,height),term_criteria)
    
    # converting of points into integers
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)

    # instead of rect we use polylines because in rect you cannot
    # perform any roation
    cv2.polylines(frame,[pts],True,(255,0,0),2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

# viewing of images
cap.release()
cv2.destroyAllWindows()