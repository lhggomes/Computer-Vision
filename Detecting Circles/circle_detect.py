import numpy as np
import cv2

"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "Detecting Circles", required=True, help="Path to image")
args = vars(ap.parse_args())
"""

# Load and clone the image for manipulation
image = cv2.imread("bottle.jpg")
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# This requires a image in 8 Bit, so need to use a single channel image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circles is not None:
    # Converting the coordinates and radius for int
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        # Draw a circle in the image
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        # Draw rectangle in the circle center
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)
