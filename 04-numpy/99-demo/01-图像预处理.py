import os
import numpy as np
import cv2


CURRENT_WORK_DIR = os.getcwd()
print("当前工作路径: ", CURRENT_WORK_DIR)

CURRENT_FILE_NAME = __file__
print("当前文件名: ", CURRENT_FILE_NAME)

img_origin_path = r"cat.jpg"

img_origin = cv2.imread(img_origin_path)     #"432.bmp"没有指定路径，是因为该图片的路径和代码的路径一致 数字0，如上图所解释。
img_h, img_w, img_c = img_origin.shape
img_np = np.array(img_origin)
img_np.tofile(CURRENT_WORK_DIR + "/imgbgr_641x401_uint8.bin")

img_np = np.fromfile(CURRENT_WORK_DIR + "/imgbgr_641x401_uint8.bin", dtype = np.uint8)
img_np = img_np.reshape(img_h, img_w, img_c) # n h w c
img_np = img_np[0:img_h, 0:img_w] # crop
img_np = cv2.resize(img_np, (img_w, img_h), interpolation = cv2.INTER_NEAREST) # resize
img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # bgr -> rgb
img_np = img_np.astype(np.float32) # to float
img_np = (img_np - 128.0) / 128.0 # normalization

img_np.tofile(CURRENT_WORK_DIR + "/imgrgb_641x401_float.bin")
cv2.imshow("test", img_np)
cv2.waitKey(0)