import cv2
import numpy as np

image1 = cv2.imread(r"C:\Users\Admin\Documents\studia\sem5\przetwarzanie obrazow\kolokwium\lab2-trackbar_operacje_na_macierzach\logo.png")
b, g, r = cv2.split(image1)
dims = [b, g, r]

const = np.uint8([255])
for i in range(3):
    out = const - dims[i]
    dims[i] = out

neg = cv2.merge(dims)
cv2.imshow('window', neg)
cv2.waitKey(0)
