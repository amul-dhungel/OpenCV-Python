import cv2 
import numpy as np 

point1 = ()
point2 = ()
drawing = False

# defining of mouse event functions
def mouse_drawing(event,x,y,flags,params):
    # need to mae global because from function, it cannot be
    # changed the value into original one
    global point1, point2, drawing
    # checks the left click responses
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x,y)
        else:
            drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x,y)

# reading of video camera
cap = cv2.VideoCapture(0)

# creating of windows frame first, becauuse setMouseCallBack
# does not detect the cv2.imshow("Frame") first.
cv2.namedWindow("Frame")

# setting of mouse event for specific frame window
cv2.setMouseCallback("Frame", mouse_drawing)


while True:
    _, frame = cap.read()

    if point1 and point2:
        cv2.rectangle(frame, point1, point2, (0,255,0))
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()