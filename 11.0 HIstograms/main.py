import cv2
import numpy as np
from matplotlib import pyplot as plt

# creating 100 * 100 matrix of zeros, which will be black color
img = np.zeros((100,100),np.uint8)

# reading image
panda = cv2.imread('red_panda.jpg')

# this will split the colorful image into
# blue, green and red version
b ,g , r = cv2.split(panda)


# drawing shapes on image
# for params just google and study the function
cv2.rectangle(img,(0,50),(100,100),255,-1)
cv2.circle(img,(50,50),25,127,thickness=-1)

# displaying of an image
cv2.imshow("Imag",panda)

# plotting a graph of numpy array
# second param is the size of the histograms
# third param is the range of colors 
plt.hist(panda.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

