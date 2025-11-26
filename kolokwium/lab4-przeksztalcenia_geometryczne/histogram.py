import cv2
import numpy as np
from matplotlib import pyplot as plt

#skala szarości
img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/strawberry.jpg",
                 cv2.IMREAD_GRAYSCALE)


hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

#3 kanały
img = cv2.imread(r"c:/Users/Admin/Documents/studia/sem5/przetwarzanie obrazow/kolokwium/lab4-przeksztalcenia_geometryczne/strawberry.jpg")
colours = ['b', 'g', 'r']

for i in range(len(colours)):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, colours[i])

plt.show()