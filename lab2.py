import cv2
import time
import numpy as np


def th(value):
   print(f"asdkjaskdjak;sdj{value}")


def fun1():
   image = cv2.imread("obraz0.jpg", cv2.IMREAD_GRAYSCALE)
   # cv2.imshow("window", image)
   # cv2.waitKey(0)
   # ret, image2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
   # cv2.imshow("window", image2)
   # cv2.waitKey(0)

   cv2.namedWindow('window')
   cv2.createTrackbar('aaaa', 'window', 0, 255, th)
   cv2.createTrackbar('bbbb', 'window', 0, 2, th)

   key = ord('a')
   while key != ord('q'):
      val = cv2.getTrackbarPos('aaaa', 'window')
      choice  = cv2.getTrackbarPos('bbbb', 'window')

      if choice == 0:
         ret, image2 = cv2.threshold(image, val, 255, cv2.THRESH_BINARY)
      elif choice == 1:
         ret, image2 = cv2.threshold(image, val, 255, cv2.THRESH_BINARY_INV)
      elif choice == 2:
         ret, image2 = cv2.threshold(image, val, 255, cv2.THRESH_TOZERO)
      
      cv2.imshow('window', image2)

      key = cv2.waitKey(10)


def fun2():
   image = cv2.imread("cube.jpg")
   
   scaled = cv2.resize(image, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST)
   cv2.imshow("window1", scaled)

   scaled = cv2.resize(image, (0,0), fx=2.75, fy=2.75, interpolation= cv2.INTER_BITS)
   cv2.imshow("window2", scaled)

   scaled = cv2.resize(image, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA)
   cv2.imshow("window3", scaled)

   scaled = cv2.resize(image, (0,0), fx=2.75, fy=2.75, interpolation=cv2.INTER_CUBIC)
   cv2.imshow("window4", scaled)


   cv2.waitKey(0)

def fun3():
   image1 = cv2.imread("putcv.png")
   image2 = cv2.imread("obraz0.jpg")

   width, height, dim = image1.shape

   image2_conv = cv2.resize(image2, dsize= (width, height))
   
   # print(image2_conv.shape)
   dst = cv2.addWeighted(image1,0.7,image2_conv,0.3,0)
   
   cv2.imshow('dst',dst)
   cv2.waitKey(0)


def fun4():
   t = time.perf_counter()
   image = cv2.imread("putcv.png")
   image = cv2.resize(image,(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
   tt = time.perf_counter()
   print(f"INTER_AREA:{(tt-t)*1000}")

   t = time.perf_counter()
   image = cv2.imread("putcv.png")
   image = cv2.resize(image,(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_BITS)
   tt = time.perf_counter()
   print(f"INTER_BITS:{(tt-t)*1000} ms")

   t = time.perf_counter()
   image = cv2.imread("putcv.png")
   image = cv2.resize(image,(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
   tt = time.perf_counter()
   print(f"INTER_CUBIC:{(tt-t)*1000} ms")

   t = time.perf_counter()
   image = cv2.imread("putcv.png")
   image = cv2.resize(image,(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
   tt = time.perf_counter()
   print(f"INTER_NEAREST:{(tt-t)*1000} ms")


def fun5(path):
   image1 = cv2.imread(path)
   b, g, r = cv2.split(image1)
   dims = [b, g, r]
   print(dims)
   const = np.uint8([255])
   for i in range(3):
      out = const - dims[i]
      dims[i] = out

   neg = cv2.merge(dims)
   cv2.imshow('asdasda', neg)
   cv2.waitKey(0)

if __name__ == "__main__":
   fun5("putcv.png")