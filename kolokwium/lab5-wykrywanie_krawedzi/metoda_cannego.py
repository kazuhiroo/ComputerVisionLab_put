import cv2
import numpy as np

def empty_callback(x):
    pass

img = cv2.imread(r"C:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab5-wykrywanie_krawedzi/shapes.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('window')
cv2.createTrackbar('param1', 'window', 100, 1000, empty_callback)
cv2.createTrackbar('param2', 'window', 100, 1000, empty_callback)

while 1:
    val1 = cv2.getTrackbarPos('param1', 'window')
    val2 = cv2.getTrackbarPos('param2', 'window')
    
    output = cv2.Canny(img, val1, val2)

    cv2.imshow('window', output)
    cv2.waitKey(10)


