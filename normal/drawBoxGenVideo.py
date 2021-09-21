import cv2
import numpy as np
import re

#### 画框 ####
color = (0, 255, 255)
width = 5 

#### 将图片保存为视频 ####
image_index_start = 0
image_index_end = 15
img_input_path = 'D:\\image\\right\\'#图像存放路径这，注意最后一个文件夹要有斜杠
video_out_path = 'D:\\image\\3.mp4'  #视频保存路径
vedio_fps = 10                       #保存视频的FPS，可以适当调整
video_size=(1920,1080)               #视频格式大小
image_format = ".BMP"                #视频格式
extract_key = r"id:(.*), cx:(.*), cy:(.*), w:(.*), h:(.*)"

filter_key = "[dsp_ml_tk1]"        
origin_file_name = "D:\\image\\data.txt"              #未过滤文本文件路径
filter_file_name = "D:\\image\\data_filter.txt"       #过滤后文件存放路径

######## 过滤文件 ########
file_origin = open(origin_file_name)               
file_filter = open(filter_file_name, "w")   
file_lines = file_origin.readlines()                    #以行形式读取文件
for line in file_lines:                                 #过滤文件
    if filter_key in line:
        file_filter.writelines(line)

file_origin.close()
file_filter.close()

file_filter = open('D:\\image\\data_filter.txt', "r")
file_lines = file_filter.readlines()
file_filter.close()

#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V' )
videoWriter = cv2.VideoWriter(video_out_path, fourcc, vedio_fps, video_size)#最后一个是保存图片的尺寸

for i in range(image_index_start, image_index_end):

    #Key_values = re.findall(r'id:(.*), cx:(.*), cy:(.*), w:(.*), h:(.*)', file_lines[i])
    Key_values = re.findall(extract_key, file_lines[i])
    id = int(Key_values[0][0])
    cx = int(Key_values[0][1])
    cy = int(Key_values[0][2])
    w = int(Key_values[0][3])
    h = int(Key_values[0][4])
    #print(id, ":", cx, cy, h, w)
    
    left_up = (int(cx - w / 2),int(cy - h / 2))
    right_down = (int(cx + w / 2),int(cy + h / 2))
    frame = cv2.imread(img_input_path+ str(i) + image_format)#读取图片
    cv2.rectangle(frame, left_up, right_down, color, width)#画框
    videoWriter.write(frame)#写入视频

print("success generate video")
videoWriter.release()

