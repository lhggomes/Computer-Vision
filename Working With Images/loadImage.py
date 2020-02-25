import cv2

#Variable to storage the Image from the disk 
imageLoad = cv2.imread("test.jpg", 0)

#Show the image on Screen
cv2.imshow("ImagemCarregada", imageLoad)

#Next Function it's to prevent the window to close before the user do it
cv2.waitKey(0)
#Function to Clear all the windows after the end of the Program
cv2.destroyAllWindows()