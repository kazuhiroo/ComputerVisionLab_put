import cv2
import numpy as np

img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab5-wykrywanie_krawedzi/ship.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.blur(img, (5,5))

edges = cv2.Canny(blur, 150, 255)
dilate = cv2.dilate(edges, (5,5), iterations=5)

cv2.imshow('window', edges)
cv2.waitKey(0)

# Kontury
# cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
lines = cv2.HoughLinesP(dilate,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('hp',img)
cv2.waitKey(0)
