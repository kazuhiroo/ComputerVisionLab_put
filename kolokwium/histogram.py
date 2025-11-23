import cv2
import numpy as np
from matplotlib import pyplot as plt


img_g = cv2.imread("strawberry.jpg", cv2.IMREAD_GRAYSCALE)
img_c = cv2.imread("strawberry.jpg")

img_g = cv2.resize(img_g, dsize=(0,0), fx=0.5, fy=0.5)
img_g = cv2.resize(img_c, dsize=(0,0), fx=0.5, fy=0.5)

hist = cv2.calcHist([img_g],[0],None,[256],[0,256])
plt.plot(hist)
plt.xlim([0,256])
plt.show()

colours = ['b','g','r']

for i, col in enumerate(colours):
    hist = cv2.calcHist([img_c],[i],None,[256],[0,256])
    plt.plot(hist, color = colours[i])
    plt.xlim([0,256])
plt.show()
print("added to test the internet")
cv2.imshow('window', img_g)
cv2.waitKey(0)