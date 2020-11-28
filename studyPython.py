# -*- coding: utf-8 -*-
import cv2
import numpy as np

print(cv2.__version__)

# 构建一张图
img = np.zeros([512, 512, 3], dtype=np.uint8)

# 遍历每个像素点，并进行赋值
for i in range(512):
    for j in range(512):
        img[i, j, :] = [i % 256, j % 256, (i + j) % 256]

print("图片\n");
# 展示图片
cv2.namedWindow('custom image', cv2.WINDOW_NORMAL)
cv2.imshow('custom image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()