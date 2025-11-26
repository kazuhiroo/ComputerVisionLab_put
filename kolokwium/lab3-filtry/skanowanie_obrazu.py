import cv2
import numpy as np
import time

# img = np.zeros([300, 300], np.uint8)
img = cv2.imread("lena_noise.png", cv2.IMREAD_GRAYSCALE)
height, width = img.shape

# Modyfikacja obrazu 
for i in range(height):
    for j in range(width):
        if i != 0 and j != 0:
            if i % 3 == 0 and j % 3 == 0:
                img[i, j] = 255

cv2.imshow('window', img)
cv2.waitKey(0)

# RĘCZNE WYGŁADZANIE 3×3
img_manual = img.copy()
img_output = img.copy()
start_manual = time.perf_counter()

for i in range(1, height-1):
    for j in range(1, width-1):
        px_sum = (
            int(img_manual[i-1, j-1]) + int(img_manual[i-1, j]) + int(img_manual[i-1, j+1]) +
            int(img_manual[i,   j-1]) + int(img_manual[i,   j]) + int(img_manual[i,   j+1]) +
            int(img_manual[i+1, j-1]) + int(img_manual[i+1, j]) + int(img_manual[i+1, j+1])
        )
        img_output[i, j] = px_sum // 9

end_manual = time.perf_counter()

manual_time = end_manual - start_manual
print(f"Czas ręcznego wygładzania: {manual_time:.6f} s")

cv2.imshow('manual', img_output)
cv2.waitKey(0)

# OpenCV blur()

img_cv = cv2.imread("lena_noise.png", cv2.IMREAD_GRAYSCALE)

start_cv = time.perf_counter()
img_cv = cv2.blur(img_cv, (3, 3))
end_cv = time.perf_counter()

cv_smooth_time = end_cv - start_cv
print(f"Czas cv2.blur: {cv_smooth_time:.6f} s")

cv2.imshow('opencv', img_cv)
cv2.waitKey(0)



# PIKSELE NA BRZEGACH SKANOWANIA RĘCZNEGO

# img_t = cv2.blur(img_output, (3,3), borderType=cv2.BORDER_REFLECT_101)
# cv2.imshow('border', img_t)
# cv2.waitKey(0)
cv2.destroyAllWindows