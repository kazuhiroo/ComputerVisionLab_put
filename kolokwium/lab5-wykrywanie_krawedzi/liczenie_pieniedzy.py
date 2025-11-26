import cv2
import numpy as np

img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab5-wykrywanie_krawedzi/coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 2)

cv2.namedWindow('window')
cv2.createTrackbar('min', 'window', 50, 100, lambda x: None)
cv2.createTrackbar('max', 'window', 50, 100, lambda x: None)

zl_r = 105
zl_val = 1

dz_gr_r = 50
dz_gr_val = 0.1

radius = [zl_r, dz_gr_r]
values = [zl_val, dz_gr_val]

img_test = img.copy()

key = ord('a')
while key != ord('q'):
    min = cv2.getTrackbarPos('min', 'window')
    max = cv2.getTrackbarPos('max', 'window')
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=150,param2=40,minRadius=min,maxRadius=max)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(img_test,(i[0],i[1]),i[2],(0,0,255),2)

    cv2.imshow('window', img_test)
    key = cv2.waitKey(10)

total_value = 0

for i in range(len(radius)):
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=150,param2=40,minRadius=radius[i],maxRadius=radius[i])
    print(len(circles[0,:]))
    total_value += len(circles[0,:])*values[i]

print(f"Total amount is: {total_value:.2f}")

