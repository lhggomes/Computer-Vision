import numpy as np 
import cv2 as cv 

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#Using the photo on a Gray Scale 
imageValid = cv.imread('tony.jpg')
grayImage = cv.cvtColor(imageValid, cv.COLOR_BGR2GRAY)
