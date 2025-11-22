import cv2
import numpy as np


blank_image = np.zeros((300,800,1), np.uint8)
h, w = blank_image.shape[:2]
for i in range(h):
    for j in range(w):
        if i%3 == 0 and j%3==0:
            blank_image[i,j] = 180

cv2.namedWindow('window')
cv2.imshow('window', blank_image)
cv2.waitKey(0)

_, img_thresh = cv2.threshold(blank_image, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('window', img_thresh)
cv2.imshow('window2', blank_image)
cv2.waitKey(0)