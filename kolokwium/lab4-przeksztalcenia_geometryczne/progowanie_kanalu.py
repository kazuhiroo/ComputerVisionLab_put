import cv2


points = []

def getCoords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append((y,x))

cv2.namedWindow('window')
cv2.setMouseCallback('window', getCoords)

img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/strawberry.jpg")

while len(points) != 2:
    cv2.imshow('window', img)
    cv2.waitKey(10)

x1, y1 = points[0]
x2, y2 = points[1]

roi = img[x1:x2, y1:y2, 1]
_, thresh = cv2.threshold(roi, 200, 255, cv2.THRESH_BINARY)

output = img.copy()
output[x1:x2, y1:y2, 1] = thresh

cv2.imshow('window', output)
cv2.waitKey(0)

