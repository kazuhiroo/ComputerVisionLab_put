import cv2 
import numpy as np

img_snp = cv2.imread("lena_snp.png")
img_noise = cv2.imread("lena_noise.png")


def empty_callback(x):
    pass

cv2.namedWindow('window')
cv2.createTrackbar('ksize', 'window', 0,50, empty_callback)

while 1:
    val = cv2.getTrackbarPos('ksize', 'window')
    size = 2*val+1

    kernel = np.ones([size, size])/(size**2)

    filtered = cv2.filter2D(img_noise,-1, kernel=kernel)
    # filtered = cv2.medianBlur(img_snp, size)
    # filtered = cv2.GaussianBlur(img_noise, (size, size), 0)

    cv2.imshow('window', filtered)
    cv2.waitKey(10)
