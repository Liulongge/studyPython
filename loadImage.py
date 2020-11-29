import cv2
import numpy as np
image_path = "D:\\image\\lena.jpg"
img = cv2.imread(image_path)
cv2.rectangle(img, (10,10), (200,200), (0, 0, 255), 3)
print("图片\n");
# 展示图片
cv2.namedWindow('custom image', cv2.WINDOW_NORMAL)
cv2.imshow('custom image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

img_root = 'F:\\test\\'#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 30    #保存视频的FPS，可以适当调整
size=(960,544)
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('F:/3.avi',fourcc,fps,size)#最后一个是保存图片的尺寸

#for(i=1;i<471;++i)
for i in range(1,327):
    frame = cv2.imread(img_root+str(i)+'.jpg')
    videoWriter.write(frame)
videoWriter.release()