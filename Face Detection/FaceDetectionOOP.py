import cv2
import os

#Global Variables
extensions = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']

class FaceDetector:
    def checkFaces(self, photo):
        image = cv2.imread(photo)


    def generateFaces(self):
        global extensions
        photosToCheck = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
        ]

        for filename in photosToCheck:
            self.checkFaces(filename)
