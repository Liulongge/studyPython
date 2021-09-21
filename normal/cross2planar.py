import cv2
import numpy as np
import struct
 
image = cv2.imread("D:\\image\\lena.jpg")
#imageClone = np.zeros((image.shape[0],image.shape[1],1),np.uint8)
 
#image.shape[0]为rows
#image.shape[1]为cols
#image.shape[2]为channels
#image.shape = (480,640,3)
rows = image.shape[0]
cols = image.shape[1]
channels = image.shape[2]
#把图像转换为二进制文件
#python写二进制文件，f = open('name','wb')
#只有wb才是写二进制文件
fileSave = open('patch.bin','wb')
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,2])
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,1])
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,0])
fileSave.close()



#把二进制转换为图像并显示
#python读取二进制文件，用rb
#f.read(n)中n是需要读取的字节数，读取后需要进行解码，使用struct.unpack("B",fileReader.read(1))函数
#其中“B”为无符号整数，占一个字节，“b”为有符号整数，占1个字节
#“c”为char类型，占一个字节
#“i”为int类型，占四个字节，I为有符号整形，占4个字节
#“h”、“H”为short类型，占四个字节，分别对应有符号、无符号
#“l”、“L”为long类型，占四个字节，分别对应有符号、无符号
fileReader = open('patch.bin','rb')
imageRead = np.zeros(image.shape,np.uint8)
for step in range(0,rows):
    for step2 in range(0,cols):
        a = struct.unpack("B",fileReader.read(1))
        imageRead[step,step2,2] = a[0]
for step in range(0,rows):
    for step2 in range(0,cols):
        a = struct.unpack("b",fileReader.read(1))
        imageRead[step,step2,1] = a[0]
for step in range(0,rows):
    for step2 in range(0,cols):
        a = struct.unpack("b",fileReader.read(1))
        imageRead[step,step2,0] = a[0]
     
fileReader.close()
cv2.imshow("source",image)
cv2.imshow("read",imageRead)
cv2.waitKey(0)
