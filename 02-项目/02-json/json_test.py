#encoding=utf-8
import json
import getopt
import sys
import os
import subprocess
import shutil

GLOBAL_PRODUCT_NAME=''
GLOBAL_MODEL_A_FILE_COPY=[]
GLOBAL_MODEL_A_MODEL_BUILD=[]
GLOBAL_MODEL_B_FILE_COPY=[]
GLOBAL_MODEL_B_MODEL_BUILD=[]


# 定义一个简单的结构体
class File_copy:
    def __init__(self, src_path, dst_path):
        self.src_path = src_path
        self.dst_path = dst_path

def file_copy(storage_list) :
    # 调用copy_file函数，传入源文件路径和目标文件路径
    for i in range(0, len(storage_list)) :
        shutil.copy(storage_list[i].src_path, storage_list[i].dst_path)
        print(storage_list[i].src_path, "->" ,storage_list[i].dst_path)

    
def model_build_parse(json_desc, storage_list) :
    for i in range(0, len(json_desc)) :
        storage_list.append(str(json_desc[str(i)]))
    
def file_copy_parse(json_desc, storage_list) :
    for i in range(0, len(json_desc)) :
        # print(json_desc[str(i)]['src_path'])
        # print(json_desc[str(i)]['dst_path'])
        storage_list.append(File_copy(str(json_desc[str(i)]['src_path']), str(json_desc[str(i)]['dst_path'])))

def parse():
    with open('desc.json', 'r') as file:
        desc = json.load(file)
        product_desc = desc[str(GLOBAL_PRODUCT_NAME)]
        
        #model a
        model_a_desc = product_desc['model_a']
        # file copy
        file_copy_parse(model_a_desc['file_copy'], GLOBAL_MODEL_A_FILE_COPY)
        for i in range(0, len(GLOBAL_MODEL_A_FILE_COPY)) :
            print(GLOBAL_MODEL_A_FILE_COPY[i].src_path, GLOBAL_MODEL_A_FILE_COPY[i].dst_path)
        # model build
        model_build_parse(model_a_desc['model_build'], GLOBAL_MODEL_A_MODEL_BUILD)
        for i in range(0, len(GLOBAL_MODEL_A_MODEL_BUILD)) :
            print(GLOBAL_MODEL_A_MODEL_BUILD[i])

        # model b
        model_b_desc = product_desc['model_b']
        file_copy_parse(model_b_desc['file_copy'], GLOBAL_MODEL_B_FILE_COPY)
        for i in range(0, len(GLOBAL_MODEL_B_FILE_COPY)) :
            print(GLOBAL_MODEL_B_FILE_COPY[i].src_path, GLOBAL_MODEL_B_FILE_COPY[i].dst_path)
        # model build
        model_build_parse(model_b_desc['model_build'], GLOBAL_MODEL_B_MODEL_BUILD)
        for i in range(0, len(GLOBAL_MODEL_B_MODEL_BUILD)) :
            print(GLOBAL_MODEL_B_MODEL_BUILD[i])


def main(argv):
    global GLOBAL_PRODUCT_NAME
    try:
        options, args = getopt.getopt(argv, "hn:", ["help", "name="])
    except getopt.GetoptError:
        sys.exit()
 
    for option, value in options:
        if option in ("-h", "--help"):
            print("help")
        if option in ("-n", "--name"):
            print("name is: {0}".format(value))
            GLOBAL_PRODUCT_NAME=value
 
if __name__ == '__main__':
    # 调用Shell命令
    output = subprocess.check_output('rm -rf ./dst_path/*', shell=True)
    main(sys.argv[1:])
    parse()
    file_copy(GLOBAL_MODEL_A_FILE_COPY)
    file_copy(GLOBAL_MODEL_B_FILE_COPY)