import cv2
import numpy as np


def empty_callback(x):
    pass

img1 = cv2.imread(r"C:\Users\Admin\Documents\studia\sem5\przetwarzanie obrazow\kolokwium\lab2-trackbar_operacje_na_macierzach\logo.png")
img2 = cv2.imread(r"C:\Users\Admin\Documents\studia\sem5\przetwarzanie obrazow\kolokwium\lab2-trackbar_operacje_na_macierzach\papug.jpg")

img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

cv2.namedWindow('window')
cv2.createTrackbar('alpha', 'window', 10, 10, empty_callback)
cv2.createTrackbar('beta', 'window', 10,  10, empty_callback)
while 1:
    alpha = cv2.getTrackbarPos('alpha', 'window')/10
    beta = cv2.getTrackbarPos('beta', 'window')/10

    output = cv2.addWeighted(img1,alpha,img2,beta,0)

    cv2.imshow('window', output)
    cv2.waitKey(10)


