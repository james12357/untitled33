import cv2
import numpy as np

img = cv2.imread("test.png")
biImg = cv2.bilateralFilter(img, 25, 25, 25)
ck = np.append(img, biImg, axis=1)  # 拼接处理前后的图像，用于对比
cv2.imshow("comparison", ck)
cv2.waitKey(0)
