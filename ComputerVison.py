#Project on Computer Vision
import numpy as np 
import cv2 as cv 

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


#Using the photo on a Gray Scale 
imageValid = cv.imread('tony.jpg')
grayImage = cv.cvtColor(imageValid, cv.COLOR_BGR2GRAY)

#Creating an Rectangle on the Face of the person
faces = face_classifier.detectMultiScale(grayImage, 1.3, 5)

for (x,y,w,h) in faces: 
    cv.rectangle(imageValid,(x,y), (x+w, y+h), (255,0,0), 2)

#Show the photo on the screen for the user

cv.imshow('imagem', imageValid)
cv.waitKey(0)
cv.destroyAllWindows()


