import cv2

img = cv2.imread('./resources/minato.png')
img = cv2.resize(img, (640, 400))[0:-50, 80:-60]
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (0, 0), 7)
# imgCanny = cv2.Canny(img, 100, 150)

# cv2.imshow('output blur', imgBlur)
cv2.imshow('output cropped', img)
# cv2.imshow('output', imgGray)
# cv2.imshow('output canny', imgCanny)
cv2.waitKey(0)
