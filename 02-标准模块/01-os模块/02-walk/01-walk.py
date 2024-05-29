# .
# ├── 00-dir
# │   ├── 1
# │   │   ├── 2
# │   │   │   ├── 3
# │   │   │   └── 4.txt
# │   │   └── 3.txt
# │   └── 2
# │       └── 3
# │           ├── 4
# │           │   └── 5.txt
# │           └── 6.txt
# └── 01-walk.py


# os.walk() 是 Python 的 os 模块中的一个非常有用的函数，它用于遍历目录树。
# 它生成给定目录中的文件名，这些目录以自顶向下的方式递归访问，同时返回目录名和子目录名。

import os

# 操作的文件夹路径
operate_path = r"./00-dir"

for root, dirs, files in os.walk(operate_path):
    print('root:',root)
    print('dirs:',dirs)
    print('files:',files)

# root: ./00-dir
# dirs: ['1', '2']
# files: []

# root: ./00-dir/1
# dirs: ['2']
# files: ['3.txt']

# root: ./00-dir/1/2
# dirs: ['3']
# files: ['4.txt']

# root: ./00-dir/1/2/3
# dirs: []
# files: []

# root: ./00-dir/2
# dirs: ['3']
# files: []

# root: ./00-dir/2/3
# dirs: ['4']
# files: ['6.txt']

# root: ./00-dir/2/3/4
# dirs: []
# files: ['5.txt']


# walk结合正则表达式从文件夹中提取期望文件
import re

pattern = r".*\.txt"
pattern = re.compile(pattern)  # 编译正则表达式

for root, dirs, files in os.walk(operate_path):
    for name in files: 
        if pattern.match(name):  # 使用正则表达式的match方法  
            print(os.path.join(root, name)) 

# ./00-dir/1/3.txt
# ./00-dir/1/2/4.txt
# ./00-dir/2/3/6.txt
# ./00-dir/2/3/4/5.txt