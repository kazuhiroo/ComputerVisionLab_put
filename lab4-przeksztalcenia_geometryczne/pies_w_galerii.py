import cv2
import numpy as np

points = []

def getCoords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append((x, y))

cv2.namedWindow('window')
cv2.setMouseCallback('window', getCoords)

img_gallery = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/gallery.png")
h_g, w_g = img_gallery.shape[:2]

img_pug = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/pug.png")
img_pug = cv2.resize(img_pug, (h_g,w_g))
h_p, w_p = img_pug.shape[:2]

while len(points) != 4:
    cv2.imshow('window', img_gallery)
    cv2.waitKey(10)

points_pug = np.float32([[0,0], [w_p,0], [0,h_p], [w_p,h_p]])
chosen_points = np.float32(points)

M = cv2.getPerspectiveTransform(points_pug, chosen_points)
transformed_pug = cv2.warpPerspective(img_pug, M, (w_g, h_g))

######## erasing the background
img_pug_gray = cv2.cvtColor(transformed_pug, cv2.COLOR_BGR2GRAY)
_, alpha = cv2.threshold(img_pug_gray, 0, 255, cv2.THRESH_BINARY)
b, g, r = cv2.split(transformed_pug)
rgba_pug = [b, g, r, alpha]

output = img_gallery.copy()
for c in range(3):  # B,G,R
    output[:,:,c] = np.where(alpha==255, transformed_pug[:,:,c], img_gallery[:,:,c])

cv2.imshow('window', output)
cv2.waitKey(0)

#### lub maska

# gray = cv2.cvtColor(transformed_pug, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)

# # Wycinamy miejsce dla psa w galerii
# roi = img_gallery.copy()
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# # Bierzemy tylko psa
# img2_fg = cv2.bitwise_and(transformed_pug, transformed_pug, mask=mask)

# dst = cv2.add(img1_bg, img2_fg)
# img_gallery[0:h_g, 0:w_g] = dst  # cały obraz lub tylko wybrany ROI

# cv2.imshow('result', img_gallery)
# cv2.waitKey(0)
# cv2.destroyAllWindows()