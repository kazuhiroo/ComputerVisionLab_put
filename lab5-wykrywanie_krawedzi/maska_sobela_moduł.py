import cv2
import numpy as np


img = cv2.imread(r"C:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab5-wykrywanie_krawedzi/einstein.jpg", cv2.IMREAD_GRAYSCALE)

maska_x = np.float32([[1, 0, -1],
                      [2, 0, -2],
                      [1, 0, -1]]) / 4

maska_y = np.float32([[1, 2, 1],
                      [0, 0, 0],
                      [-1, -2, -1]]) / 4


img_fx = cv2.filter2D(img, -1, maska_x)
img_fy = cv2.filter2D(img, -1, maska_y)

cv2.imshow('mx', img_fx)
cv2.imshow('my', img_fy)
cv2.waitKey(0)


mod_g = np.sqrt(np.float32(img_fx)**2 + np.float32(img_fy)**2)
mod_g = mod_g / np.amax(mod_g) * 255.0
mod_g = mod_g.astype(np.uint8)

cv2.imshow("Modul gradientu", mod_g)
cv2.waitKey(0)