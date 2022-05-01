import cv2
import numpy as np

image = cv2.imread("./flag.png")
image2 = cv2.imread("/home/amul/OpenCV Learning/3.0 Drawing on images/red_panda.jpg")

# system reads the image in the form of array.
# image is basically a set of pixel value
# if all pixel values are included in np.array and opened
# with image function, it will display the image

print(image.shape)
print(image[175,200])

# changing the rgb color of pixel values
image[175,200] = (0,255,0)
image[175,201] = (0,255,0)
image[175,203] = (0,255,0)
image[175,202] = (0,255,0)
image[175,204] = (0,255,0)
image[175,205] = (0,255,0)
image[175,206] = (0,255,0)

# displaying image through set of pixels

row,cols,ch = image2.shape
roi = image2[0:row,0:cols,2]
cv2.imshow("Flag",image)
cv2.imshow("Panda",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()