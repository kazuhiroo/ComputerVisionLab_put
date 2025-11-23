import cv2
import numpy as np


img = cv2.imread("fruits.jpg")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

apple_min = np.array([35, 40, 60])
apple_max = np.array([100, 255, 255])
orange_min = np.array([10, 74, 79])
orange_max = np.array([25, 255, 255])

mask_apple = cv2.inRange(img_hsv, apple_min, apple_max)
mask_orange = cv2.inRange(img_hsv, orange_min, orange_max)

apple_img = cv2.bitwise_and(img, img, mask=mask_apple)
orange_img = cv2.bitwise_and(img, img, mask=mask_orange)

apple_gray = cv2.cvtColor(apple_img, cv2.COLOR_BGR2GRAY)
orange_gray = cv2.cvtColor(orange_img, cv2.COLOR_BGR2GRAY)

_, apple_thresh = cv2.threshold(apple_gray, 0, 255, cv2.THRESH_BINARY_INV)
_, orange_thresh = cv2.threshold(orange_gray, 0, 255, cv2.THRESH_BINARY_INV) 

apple_thresh = cv2.GaussianBlur(apple_thresh, (9,9), 0)
orange_thresh = cv2.GaussianBlur(orange_thresh, (9,9), 0)

circles_apple = cv2.HoughCircles(apple_thresh, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=45, minRadius=0, maxRadius=0)
circles_orange = cv2.HoughCircles(orange_thresh, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=50, minRadius=0, maxRadius=0)

circles_apple = np.uint16(np.around(circles_apple))
for i in circles_apple[0,:]:
        x, y, r = i[0], i[1], i[2]
        cv2.rectangle(img, (x-r, y-r), (x+r, y+r), (255,0,0), 2)


circles_orange = np.uint16(np.around(circles_orange))
for i in circles_orange[0,:]:
        x, y, r = i[0], i[1], i[2]
        cv2.rectangle(img, (x-r, y-r), (x+r, y+r), (255,255,0), 2)


cv2.imshow('window', img)
cv2.waitKey(0)