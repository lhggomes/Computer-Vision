import numpy as np
import cv2

"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "Detecting Circles", required=True, help="Path to image")
args = vars(ap.parse_args())
"""

image = cv2.imread("bottle.jpg")
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Gray Scale

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255,0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128,255), -1)

    cv2.imshow("output", np.hstack([image, output]))
    cv2.imwrite("Image.jpg", output)
    cv2.waitKey(0)

