import cv2
import numpy as np 

#Reading an Image from the Disk
soccerPicture = cv2.imread('soccer.jpg')

#Printing the data of the picture
print (soccerPicture.shape)

#Show the information about the Pixels 
print (soccerPicture.item(0,0,1)) # 0 = Blue Channel / 1 = Green Channel / 2 = Red Channel 

#Changing the Pixels 
soccerPicture.itemset((0,0,2), 255)  #First is the positon, then the new RGB Color
soccerPicture.itemset((0,0,1), 0) 
soccerPicture.itemset((0,0,0), 0) 
cv2.imwrite("soccer2.jpg", soccerPicture)

#Region of interest 
ball = soccerPicture[180:250, 250:315] #Fist the range of Y then the range of X
soccerPicture[130:200, 200:265] = ball #Define the range to copy, than add it 
cv2.imwrite('ball.jpg', soccerPicture)
