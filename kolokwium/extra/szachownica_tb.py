import cv2
import numpy as np

cv2.namedWindow('window')
cv2.createTrackbar('tiles_size', 'window', 2, 50, lambda x: None)  # liczba kratek
cv2.createTrackbar('color', 'window', 0, 1, lambda x: None)

key = ord('a')
while key != ord('q'):
    color = cv2.getTrackbarPos('color', 'window')
    num_tiles = cv2.getTrackbarPos('tiles_size', 'window')
    
    if num_tiles < 1:
        num_tiles = 1

    img_size = 500
    tile_size = img_size // num_tiles  # całkowity rozmiar kafelka

    # tworzymy pusty obraz
    img = np.ones((tile_size*num_tiles, tile_size*num_tiles), dtype=np.uint8) * color * 255

    for i in range(num_tiles):
        for j in range(num_tiles):
            if (i + j) % 2 == 0:
                img[i*tile_size:(i+1)*tile_size, j*tile_size:(j+1)*tile_size] = (1-color)*255

    cv2.imshow('window', img)
    key = cv2.waitKey(10)
