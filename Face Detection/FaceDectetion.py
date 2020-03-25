import cv2
# Loading the XML from
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Reading the img from the disk
img = cv2.imread('parAperam.jpg')
# Convert the image to Gray Scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faceImage = faceCascade.detectMultiScale(gray, 1.1, 4)
#Draw the rectangle
for (x, y, w, h) in faceImage:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
cv2.imshow('Test', img)
cv2.waitKey()
cv2.destroyAllWindows()
