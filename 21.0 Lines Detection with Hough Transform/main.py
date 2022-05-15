import cv2
import numpy as np

# reading of images
img = cv2.imread("lines.jpg")
# changes of images into gray color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges detection 
edges = cv2.Canny(gray, 75, 150)

# it is used to detected lines, edges, cordinates
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30,maxLineGap=250)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0),3)

cv2.imshow("Images",img)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()