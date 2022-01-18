import cv2
import numpy as np


def preProcess(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    # imgDial = cv2.dilate(imgCanny, np.ones((5, 5)), iterations=2)
    # imgThres = cv2.erode(imgDial, np.ones((5, 5)), iterations=1)
    return imgCanny


cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (640, 480))
    imgThres = preProcess(img)
    cv2.imshow("Result", imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
