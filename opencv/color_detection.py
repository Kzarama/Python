import cv2 as cv
import numpy as np


def empty(num):
    pass


path = "./resources/minato.png"
cv.namedWindow("TrackBars", cv.WINDOW_AUTOSIZE)
cv.resizeWindow("TrackBars", 640, 200)
cv.createTrackbar("Hue min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue max", "TrackBars", 179, 179, empty)
cv.createTrackbar("Sat min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Sat max", "TrackBars", 255, 255, empty)
cv.createTrackbar("Val min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Val max", "TrackBars", 255, 255, empty)

while True:
    img = cv.imread(path)
    img = cv.resize(img, (600, 350))
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv.getTrackbarPos("Val min", "TrackBars")
    v_max = cv.getTrackbarPos("Val max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    imgResult = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("Original", img)
    cv.imshow("result", imgResult)
    cv.imshow("Mask", mask)
    cv.waitKey(1)
