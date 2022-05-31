import cv2 
import numpy as np
from sklearn import neighbors 

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

# using of harcascade xml file for detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cv2.namedWindow("Frame")
cv2.createTrackbar("Neighbours", "Frame", 5,20,nothing)


while True:
    _, frame = cap.read()

    # changing of image into gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    neighbours = cv2.getTrackbarPos("Neighbours", "Frame")

    faces = face_cascade.detectMultiScale(gray, 1.3, neighbours)

    # plotting of rectangle around faces
    for rect in faces:
        (x,y,w,h) = rect
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0,255,0),2)



    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()