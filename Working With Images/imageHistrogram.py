import cv2
import numpy as np
from matplotlib import pyplot as plt 

image = cv2.imread("soccer.jpg", 0)
plt.hist(image.ravel(), 256, [0,256])
cv2.imshow("Imagem Original", image)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()