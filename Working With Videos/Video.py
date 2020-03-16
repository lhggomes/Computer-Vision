import cv2
import numpy as np
cap = cv2.VideoCapture(0)
countBalada = 0

while True:
    existeFrame, frame = cap.read()

    altura, largura, _ = frame.shape
    imgEmpty = np.zeros((altura, largura), dtype = "uint8")

    (B, G, R) = cv2.split(frame)

    R = cv2.merge([imgEmpty, imgEmpty, R])
    G = cv2.merge([imgEmpty, G, imgEmpty])
    B = cv2.merge([B, imgEmpty, imgEmpty])

    imgBalada = np.zeros((altura, largura,3), dtype="uint8")

    countBalada = countBalada % 4
    countBalada += 1

    if countBalada == 0:
        imgBalada = frame
    elif countBalada == 1:
        imgBalada = R
    elif countBalada == 2:
        imgBalada = G
    elif countBalada == 3:
        imgBalada = B

    #Showing the video Captured from the WebCAM
    cv2.imshow("WebCam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #Showing the Video from the Modify Files

    cv2.imshow("WebCam Balada", imgBalada)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()