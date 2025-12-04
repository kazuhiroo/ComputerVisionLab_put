import cv2
import numpy as np

img = cv2.imread("road.jpg")
img = cv2.resize(img, dsize=(0,0), fx=0.5, fy=0.5)

h, w = img.shape[:2]
print(h, w)
points = []
points2 = np.float32([[0,0],[w,0],[0,h],[w,h]])

def GetCord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        points.append([x,y])
    
cv2.namedWindow('window')
cv2.setMouseCallback('window', GetCord)

while 1:
    cv2.imshow('window', img)

    if len(points) == 4:
        points1 = np.float32(points)
        M = cv2.getPerspectiveTransform(points1, points2)
        output = cv2.warpPerspective(img, M, (w, h))
        break;
    
    cv2.waitKey(10)


cv2.imshow('window', output)
cv2.waitKey(0)