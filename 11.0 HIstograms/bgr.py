import cv2
import numpy as np
from matplotlib import pyplot as plt


# reading image
panda = cv2.imread('red_panda.jpg')

# this will split the colorful image into
# blue, green and red version
b ,g , r = cv2.split(panda)



# displaying of an image
cv2.imshow("panda",panda)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)


# plotting a graph of numpy array
# second param is the size of the histograms
# third param is the range of colors 
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

