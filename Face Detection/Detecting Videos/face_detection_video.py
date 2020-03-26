import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_file = ''
cap = cv2.VideoCapture(video_file)

