import cv2
import numpy as np


points = []

img_dog = cv2.imread("dog.png")
img_gallery = cv2.imread("gallery.png")

h_gallery, w_gallery = img_gallery.shape[:2]
h_dog, w_dog = img_dog.shape[:2]

def getPoints(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append((x,y))


cv2.namedWindow('window')
cv2.setMouseCallback('window', getPoints)

key = ord('a')

while key != ord('q'):
    cv2.imshow('window', img_gallery)

    if len(points) == 4:
        points0 = np.float32([[0,0],[w_dog,0],[0,h_dog],[w_dog,h_dog]])
        points1 = np.float32(points)
        
        M = cv2.getPerspectiveTransform(points0, points1)
        output = cv2.warpPerspective(img_dog, M, (w_gallery, h_gallery))
        
        # mask  
        dog_grey = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(dog_grey, 5, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        roi = img_gallery.copy()
        background = cv2.bitwise_and(roi, roi, mask=mask_inv)
        dog_foreground = cv2.bitwise_and(output, output, mask=mask)

        dst = cv2.add(background, dog_foreground)
        break


    key = cv2.waitKey(10)


cv2.imshow('window', dst)
cv2.waitKey(0)