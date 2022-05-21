import cv2 
import numpy as np 


# defining of mouse event functions
def mouse_drawing(event,x,y,flags,params):
    # checks the left click responses
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("left click")
        # print(event,x,y)
        circle.append((x,y))
    
# reading of video camera
cap = cv2.VideoCapture(0)

# creating of windows frame first, becauuse setMouseCallBack
# does not detect the cv2.imshow("Frame") first.
cv2.namedWindow("Frame")

# setting of mouse event for specific frame window
cv2.setMouseCallback("Frame", mouse_drawing)

# setting of postiions in list.
circle = []
while True:
    _, frame = cap.read()

    # adding of circle center when button is clicked
    for center_position in circle:
        print(center_position)
        cv2.circle(frame, center_position, 3, (0,255,0),-1)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("d"):
        circle = []

cap.release()
cv2.destroyAllWindows()