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

fruit_size = 100

M = cv2.moments(mask_apple)

cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])

cv2.rectangle(img, (cx - fruit_size, cy - fruit_size), (cx + fruit_size, cy + fruit_size), (255, 0, 0), 2)

M = cv2.moments(mask_orange)

cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])

cv2.rectangle(img, (cx - fruit_size, cy - fruit_size), (cx + fruit_size, cy + fruit_size), (0, 255, 0), 2)

cv2.imshow('window', img)
cv2.waitKey(0)