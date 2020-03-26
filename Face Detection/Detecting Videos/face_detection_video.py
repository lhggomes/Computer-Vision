import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_file = 'vasilha.mp4'
cap = cv2.VideoCapture('vasilha.mp4')

while True:
    #Reading the Frame
    img = cap.read()
    #Gray Scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Detect Faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #Draw for each face
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
