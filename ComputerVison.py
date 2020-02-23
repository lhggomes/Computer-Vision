import numpy as np 
import cv2 as cv 

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

imageValid = cv.imread('image')
