import cv2
from matplotlib import pyplot as plt


img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/strawberry.jpg", cv2.IMREAD_GRAYSCALE)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# clahe = cv2.createCLAHE()

cl1 = clahe.apply(img)

cv2.imshow('window', cl1)
cv2.waitKey(0)