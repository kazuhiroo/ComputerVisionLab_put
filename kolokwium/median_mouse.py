import cv2

temp = []

def GetCord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        temp.append((x,y)) 
        print(x,y)

cv2.namedWindow('window')
img = cv2.imread("image.jpg")
img_scaled = cv2.resize(img, dsize=(0,0), fx=2, fy=2)

cv2.setMouseCallback('window', GetCord)

while 1:
    cv2.imshow('window', img_scaled)
    if len(temp) == 2:

        y1, x1 = temp[0]
        y2, x2 = temp[1]

        y_min, y_max = sorted([y1, y2])
        x_min, x_max = sorted([x1, x2])

        img_filtered = cv2.medianBlur(img_scaled[x_min:x_max, y_min:y_max], 9)
        img_scaled[x_min:x_max, y_min:y_max] = img_filtered 

        print(temp)

        break
    
    if cv2.waitKey(10) == 27:
        exit()


cv2.imshow('window', img_scaled)
cv2.waitKey(0)