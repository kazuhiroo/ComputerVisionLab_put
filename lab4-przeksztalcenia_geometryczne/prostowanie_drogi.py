import cv2
import numpy as np

points = []

def getCoords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append((x,y))


cv2.namedWindow('window')
cv2.setMouseCallback('window', getCoords)

img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/road.jpg")
img = cv2.resize(img, dsize=(0,0), fx=0.4, fy=0.4)
height, width = img.shape[:2]

while len(points) != 4:
    cv2.imshow('window', img)
    cv2.waitKey(10)

destined_pts = np.float32([[0,0],[width, 0],[0, height],[width,height]])
chosen_pts = np.float32(points)

M = cv2.getPerspectiveTransform(chosen_pts, destined_pts)
output = cv2.warpPerspective(img, M, (width, height))

cv2.imshow('window', output)
cv2.waitKey(0)