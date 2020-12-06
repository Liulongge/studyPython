import cv2
import numpy as np
image_path = "D:\\image\\lena.jpg"

#### 画框 ####
img = cv2.imread(image_path)
left_up = (100,100)
right_down = (400,400)
color = (0, 255, 255)
width = 5 
cv2.rectangle(img, left_up, right_down, color, width)

#### 展示图片 ####
cv2.namedWindow('custom image', cv2.WINDOW_NORMAL)
cv2.imshow('custom image', img)
cv2.imwrite("F:\\1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#### 将图片保存为视频 ####
img_input_path = 'D:\\image\\right\\'#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
video_out_path = 'D:\\image\\3.mp4'
vedio_fps = 10    #保存视频的FPS，可以适当调整
video_size=(1920,1080)
image_index_start = 0
image_index_end = 50
image_format = ".BMP" 

#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V' )
videoWriter = cv2.VideoWriter(video_out_path, fourcc, vedio_fps, video_size)#最后一个是保存图片的尺寸

for i in range(image_index_start, image_index_end):
#    frame = cv2.imread(img_input_path+str(i)+'.jpg')
    frame = cv2.imread(img_input_path+ str(i) + image_format)
    videoWriter.write(frame)
videoWriter.release()

