import numpy as np
import cv2

# 入出力フォルダ
input_file = './input.jpg'
output_file = './out_Haar_like.jpg'

# 分類器の特徴量を取得する
faceCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_fullbody.xml')

# ファイル読み込み
image = cv2.imread(input_file,cv2.IMREAD_COLOR)

# リサイズ
finalHeight = 800.0
scale = finalHeight / image.shape[0]
image = cv2.resize(image, None, fx=scale, fy=scale)

# 物体認識（人）の実行
facerect = faceCascade.detectMultiScale(image, scaleFactor=1.01, minNeighbors=1, minSize=(30, 30))

#検出した人を囲む矩形の作成
for x, y, w, h in facerect:    
    cv2.rectangle(image, (x, y),(x+w, y+h),(0,255,0), 2)

cv2.imshow("results human detect by def detector", image)
cv2.waitKey(0)

# ファイルを保存
cv2.imwrite(output_file, image)