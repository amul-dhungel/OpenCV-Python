import cv2
import numpy as np

# template matching is technique of matching sections of one image
# to other images  to check the similarity.
# reading of images
img = cv2.imread('simpsons.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread('barts_face.jpg',cv2.IMREAD_GRAYSCALE)
# Inverse the rows, and columns of an image shape.
w, h = template.shape[::-1]

# displaying of result
result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.6)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0] + w, pt[1] + h), (0, 255, 0), 3)


cv2.imshow("img",img)
cv2.imshow("Result",result)



cv2.waitKey(0)
cv2.destroyAllWindows()