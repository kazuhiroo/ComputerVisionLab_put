import cv2
import numpy as np

img = cv2.imread(r"C:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab5-wykrywanie_krawedzi/shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('window')
cv2.createTrackbar('param1', 'window', 100, 1000, lambda x: None)
cv2.createTrackbar('param2', 'window', 100, 1000, lambda x: None)

key = ord('a')
while key != ord('q'):
    val1 = cv2.getTrackbarPos('param1', 'window')
    val2 = cv2.getTrackbarPos('param2', 'window')
    
    edges = cv2.Canny(img, val1, val2, apertureSize=3)

    cv2.imshow('window', edges)
    key = cv2.waitKey(10)

lines = cv2.HoughLines(edges, 1, np.pi/180, 255)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
 
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 
cv2.imshow('houghlines3',img)
cv2.waitKey(0)


cimg = cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,
                            param1=150,param2=50,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
 
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)


edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
 
cv2.imshow('hp',img)
cv2.waitKey(0)