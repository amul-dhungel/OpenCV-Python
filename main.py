# this is an openCV libarary with alias "cv2"
import cv2

# reading images with built in function of cv2 
# storing it in variables
image = cv2.imread("./red_panda.jpg")

# converting image to gray scale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# showing in image in new window, with imshow(titlename,file)
cv2.imshow("Gray panda",gray_image)
cv2.imshow("REd panda",image)

# storing the image in the form of file, with name
cv2.imwrite("gray_panda.jpg",gray_image)

# waitkey, delays the image opening time, but 0 means forever
cv2.waitKey(0)

cv2.destroyAllWindows()