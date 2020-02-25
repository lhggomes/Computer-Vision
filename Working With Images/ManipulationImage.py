import cv2
import numpy as np 

#Reading an Image from the Disk
soccerPicture = cv2.imread('soccer.jpg')

#Printing the data of the picture
print (soccerPicture.shape)

#Show the information about the Pixels 
print (soccerPicture.item(0,0,1)) # 0 = Blue Channel / 1 = Green Channel / 2 = Red Channel 