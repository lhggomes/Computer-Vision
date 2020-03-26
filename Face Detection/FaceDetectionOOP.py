import cv2
import os

# Global Variables
extensions = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']
xml_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



class FaceDetector:
    def check_faces(self, photo):
        image = cv2.imread(photo)
        # Procedure to Generate the Name of the file
        file_new_name = photo + "checked" + "jpg"
        cv2.imwrite(file_new_name, self.generate_edit_image(photo))

    # Looking for all files on a Directory

    def generate_edit_image(self, image):
        global xml_detector
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_image = xml_detector.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in face_image:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return face_image

    def generate_faces(self):
        global extensions
        photos_to_check = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
        ]
        for filename in photos_to_check:
            self.check_faces(filename)


faces = FaceDetector()
faces.generate_faces()
