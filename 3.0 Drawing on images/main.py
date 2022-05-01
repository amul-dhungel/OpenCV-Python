import cv2
import numpy as np

# reading image path
image = cv2.imread("./red_panda.jpg")

# finding shape of image
shape = image.shape
print(shape)

points = np.array([[[100,10],[30,120],[70,20],[150,60]]],np.int32)

# drawing lines on image
cv2.line(image,(10,100),(100,10),color = (255,0,0),thickness =5)

# drawing circle on image
cv2.circle(image,(20,80),20,(255,0,0),5)
cv2.rectangle(image,(50,60),(450,95),(0,0,255),-1)
# cv2.ellipse()
cv2.polylines(image,[points],True,(180,180,0),thickness=3)


# putting text on images
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"Panda",(30,100),font,4,(255,255,255))
# displaying images
cv2.imshow("Red panda",image)

cv2.waitKey(0)
cv2.destroyAllWindows()