import cv2
input_img = cv2.imread(r"D:\myCode\lena.jpg")
cv2.namedWindow("imshow", cv2.WINDOW_AUTOSIZE)
cv2.imshow("imshow",input_img)
print("data type: ", input_img.dtype)
print("image shape: ", input_img.shape)
print("image size byte: ", input_img.size)
print("image type: ", type(input_img))


#### 读取相机图像 ####
capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)# 翻转画面
    cv2.imshow("video", frame)
    c = cv2.waitKey(50) # 捕获Esc之后退出
    if c == 27:
        break
cv2.destroyAllWindows()
capture.release()
