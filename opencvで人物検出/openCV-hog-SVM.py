#https://qiita.com/nanako_ut/items/13849bd4cc087139a40c
import numpy as np
import cv2

#入出力ファイル
input_file = './input.jpg'
output_file = './output_hog_SVM.jpg'

# ファイル読込
image = cv2.imread(input_file ,cv2.IMREAD_COLOR)

hog = cv2.HOGDescriptor()
hog = cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9)

# SVMによる人検出
hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

# リサイズした方が精度がよかった
finalHeight = 800.0
scale = finalHeight / image.shape[0]
image = cv2.resize(image, None, fx=scale, fy=scale)

# 人を検出した座標
human, r = hog.detectMultiScale(image, hitThreshold = 0.6, winStride = (8,8), padding = (32, 32), scale = 1.05, finalThreshold=2)

# 全員のバウンディングボックスを作成
for (x, y, w, h) in human:
    cv2.rectangle(image, (x, y),(x+w, y+h),(0,255,0), 2)

cv2.imshow("results human detect by def detector", image)
cv2.waitKey(0)

# ファイルを保存
cv2.imwrite(output_file , image)
