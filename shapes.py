import cv2
import numpy as np


img = cv2.imread("shapes.jpg")
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=100, param2=50, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles', img)
cv2.waitKey(0)

# gray = cv2.GaussianBlur(gray, (5,5), 0)
# edges = cv2.Canny(gray,10,150,apertureSize = 3)

# cv2.imshow('window', edges)
# cv2.waitKey(0)

# lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=10, minLineLength=5, maxLineGap=5)

# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)







 
# cv2.imshow('window', img)
# cv2.waitKey(0)

