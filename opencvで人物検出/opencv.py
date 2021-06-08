#https://qiita.com/ymmtr6/items/c16cd67ce9be88820bd8


import cv2

img = cv2.imread("input.jpg")
detector = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = detector.detectMultiScale(gray_img,scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
for (x, y, w, h) in face:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 300), 4)
cv2.imwrite("output.jpg", img)
cv2.imshow("results human detect by def detector", img)
cv2.waitKey(0)


img_ = cv2.imread("input.jpg")
hog_ = cv2.HOGDescriptor()
hog_.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}
human, r = hog_.detectMultiScale(img_, **hogParams)
for (x, y, w, h) in human:
  cv2.rectangle(img_, (x, y), (x+w, y+h), (0, 0, 300), 4)
cv2.imshow("results human detect by def detector", img_)
cv2.waitKey(0)

