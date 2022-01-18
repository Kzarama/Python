import cv2
import numpy as np

path = './resources/shapes.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

imgConcat = cv2.hconcat([img, imgCanny])

cv2.imshow('original', imgConcat)
# cv2.imshow('original', img)

cv2.waitKey(0)
