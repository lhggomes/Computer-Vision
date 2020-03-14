import cv2
import numpy as np
from matplotlib import pyplot as plt 

#Reading the Image from the disk 
image = cv2.imread("soccer.jpg", 0) 
#Crating the histogram
#In this function, We needed to use another funciont (ravel) to transform the data from a matrice 2x2 to a Vector
plt.hist(image.ravel(), 256, [0,256])
cv2.imshow("Imagem Original", image)
#Show the data in the screen 
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

#ColorFull Histogram 

imageColor = cv2.imread("soccer.jpg")
color = ('b', 'g', 'r') #List of Colors of Histogram

for i, col in enumerate(color): 
   histogram = cv2.calcHist([imageColor], [i], None, [256], [0,256])
   #We used an function to calc the histogram using OpenCV
   plt.plot(histogram, color = col)
   plt.xlim([0,256])

#Showing the data on the screen
cv2.imshow("Imagaem Original", imageColor)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

#Test
