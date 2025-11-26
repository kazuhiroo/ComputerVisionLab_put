import cv2
import numpy as np

img = cv2.imread("lena_noise.png", cv2.IMREAD_GRAYSCALE)
height, width = img.shape

L = 5
output = np.zeros_like(img)
offset = L // 2
img_copy = cv2.copyMakeBorder(img, offset, offset, offset, offset, cv2.BORDER_REFLECT_101)


for i in range(height):
    for j in range(width):
        window = img_copy[i:i+L, j:j+L]

        mid = (L + 1) // 2
        q1 = window[0:mid, 0:mid]  # NW
        q2 = window[0:mid, mid:L]  # NE
        q3 = window[mid:L, 0:mid]  # SW
        q4 = window[mid:L, mid:L]  # SE

        quad = [q1, q2, q3, q4]

        vars = [np.var(q) for q in quad]
        min_idx = np.argmin(vars)
        output[i, j] = int(np.mean(quad[min_idx]))

cv2.imshow("kuwahara filter", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
