import cv2
import numpy as np


#EROZJA

img1 = np.ones([500,500])*255
height, width = img1.shape

for i in range(height):
    for j in range(width):
        if i%50 == 0 and j%50 == 0:
            img1[i, j] = 0

kernel = np.ones((5,5), np.uint8)
img1 = cv2.erode(img1, kernel)

cv2.imshow('window-erozja', img1)
cv2.waitKey(0)

#DYLATACJA

img2 = np.zeros([500,500])
height, width = img2.shape

for i in range(height):
    for j in range(width):
        if i%50 == 0 and j%50 == 0:
            img2[i, j] = 255

kernel = np.ones((5,5), np.uint8)
img2 = cv2.dilate(img2, kernel)

cv2.imshow('window-dylatacja', img2)
cv2.waitKey(0)


#OTWARCIE

img2 = np.zeros([500,500])
height, width = img2.shape

for i in range(height):
    for j in range(width):
        if i%50 == 0 and j%50 == 0:
            img2[i, j] = 255

kernel = np.ones((5,5), np.uint8)
img2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)

cv2.imshow('window-opening', img2)
cv2.waitKey(0)


#ZAMKNIĘCIE

img2 = np.zeros([500,500])
height, width = img2.shape

for i in range(height):
    for j in range(width):
        if i%50 == 0 and j%50 == 0:
            img2[i, j] = 255

kernel = np.ones((5,5), np.uint8)
img2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

cv2.imshow('window-closing', img2)
cv2.waitKey(0)