import cv2

def fun1():
   path = "obraz.jpg"
   image = cv2.imread(path)
   cv2.imshow("window", image)
   cv2.waitKey(0)

def fun2():
   path = "obraz.jpg"
   image = cv2.imread(path)
   px = image[200, 270, 0]
   print(f"Value on the coloured picture: {px}")

   image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   cv2.imshow("window", image)
   cv2.waitKey(0)
   # print(image.shape)

   px = image[220,270]
   print(f"Value on the gray-scaled picture: {px}")

def fun3():
   path = "obraz.jpg"
   image = cv2.imread(path)
   # print(image.shape)
   roi = image[100:200, 200:300]
   image[50:150, 100:200] = roi 
   cv2.imshow("roi", roi)
   cv2.imshow("window", image)
   cv2.waitKey(0)

def fun4():
   path = "obraz.jpg"
   image = cv2.imread(path)
   image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

   cv2.imshow("bgr", image)
   cv2.imshow("rgb", image2)
   cv2.waitKey(0)

def fun5():
   path = "AdditiveColor.png"
   image = cv2.imread(path)
   b, g, r = cv2.split(image)
   cv2.imshow("blue", b)
   cv2.imshow("green", g)
   cv2.imshow("red", r)
   
   im_merged = cv2.merge([b,g,r])
   cv2.imshow("merged", im_merged)
   cv2.waitKey(0)


def fun6():
    cap = cv2.VideoCapture(0)  # open the default camera

    key = ord('a')
    while key != ord('q'):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame comes here
        # Convert RGB image to grayscale
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blur the image
        img_filtered = cv2.GaussianBlur(img_gray, (7, 7), 1.5)
        # Detect edges on the blurred image
        img_edges = cv2.Canny(img_filtered, 0, 30, 3)

        # Display the result of our processing
        cv2.imshow('result', img_edges)
        # Wait a little (30 ms) for a key press - this is required to refresh the image in our window
        key = cv2.waitKey(30)

    # When everything done, release the capture
    cap.release()
    # and destroy created windows, so that they are not left for the rest of the program
    cv2.destroyAllWindows()

def fun7():
   cap = cv2.VideoCapture(0)
   key = ord('a')
   ret, frame = cap.read()
   while key != ord('q'):
      if key == ord('f'):
         ret, frame = cap.read()
         print("frame captured")
      cv2.imshow("result", frame)
      key = cv2.waitKey(30)

   cap.release()
   cv2.destroyAllWindows()

def fun8():
   video = cv2.VideoCapture('Wildlife.mp4')

   while video.isOpened():
      ret, frame = video.read()
      
      cv2.imshow("movie", frame)
      if cv2.waitKey(30) == ord('q'):
         break

   video.release()
   cv2.destroyAllWindows()

def fun9():
   images = []

   for i in range(3):
      file = f"obraz{i}.jpg"
      image = cv2.imread(file)
      images.append(image)

   key = ord('a')
   i = 0
   while key != ord('q'):
      cv2.imshow("show", images[i])
      key = cv2.waitKey(10)

      if key == ord('a'):
         if i == 2:
            i = 0 
         else:
            i += 1
         print(i)
      
      elif key == ord('d'):
         if i == 0:
            i = 2
         else:
            i -= 1
         print(i)
         
if __name__ == "__main__":
   fun9()