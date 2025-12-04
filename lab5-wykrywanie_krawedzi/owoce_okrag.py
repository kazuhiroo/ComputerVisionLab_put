import cv2
import numpy as np

img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab5-wykrywanie_krawedzi/fruits.jpg")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

apple_min = np.array([35, 40, 60])
apple_max = np.array([100, 255, 255])
orange_min = np.array([10, 74, 79])
orange_max = np.array([25, 255, 255])

apple_mask = cv2.inRange(img_hsv, apple_min, apple_max)
orange_mask = cv2.inRange(img_hsv, orange_min, orange_max)

apple_blur = cv2.GaussianBlur(apple_mask, (9, 9), 2)
orange_blur = cv2.GaussianBlur(orange_mask, (9, 9), 2)

# cv2.imshow('window',apple_blur)
# cv2.waitKey(0)

img_rect = img.copy()

apple_circles = cv2.HoughCircles(apple_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=150,param2=40,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(apple_circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)

orange_circles = cv2.HoughCircles(orange_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=150,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(orange_circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(255,255,0),2)

cv2.imshow('window', img)
cv2.waitKey(0)

circles = np.uint16(np.around(orange_circles))
for i in circles[0,:]:
        x, y, r = i[0], i[1], i[2]
        cv2.rectangle(img_rect, (x-r, y-r), (x+r, y+r), (255,0,0), 2)

circles = np.uint16(np.around(apple_circles))
for i in circles[0,:]:
        x, y, r = i[0], i[1], i[2]
        cv2.rectangle(img_rect, (x-r, y-r), (x+r, y+r), (0,0,255), 2)


cv2.imshow('window', img_rect)
cv2.waitKey(0)