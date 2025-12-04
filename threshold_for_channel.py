import cv2
import numpy as np

points = []

def getPoints(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append((x, y))

cv2.namedWindow('window')
cv2.setMouseCallback('window', getPoints)

img = cv2.imread("strawberry.jpg")

key = cv2.waitKey(1) & 0xFF
while key != ord('q'): 
    cv2.imshow('window', img)
    if len(points) == 2:

        x1, y1 = points[0]
        x2, y2 = points[1]

        x_min, x_max = sorted([x1,x2])
        y_min, y_max = sorted([y1,y2])

        img_t = img[y_min:y_max, x_min:x_max, 1]
        _, threshold = cv2.threshold(img_t, 255, 255, cv2.THRESH_BINARY)
        
        img[y_min:y_max, x_min:x_max, 1] = threshold

        points = []

    key = cv2.waitKey(10)


cv2.imshow('window', img)
cv2.waitKey(0)

