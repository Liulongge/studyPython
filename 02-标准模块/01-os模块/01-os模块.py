# 参考： 
# https://blog.csdn.net/haiming0415/article/details/126203126?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-126203126-blog-108047966.235^v38^pc_relevant_sort_base2&spm=1001.2101.3001.4242.1&utm_relevant_index=3

import os
# os模块是Python中整理文件和目录最为常用的模块，该模块提供了非常丰富的方法用来处理文件和目录。

# 1 系统模块
print('----------------------- 系统模块 -----------------------')
# 1.1 获取系统名称. nt: windows系统 posix: Linux系统
print('获取系统名称:', os.name)
# 1.2 获取系统的换行符
print('获取系统的换行符:', os.linesep)
# 1.3 获取当前系统的路径分隔符. windows下路径分隔符：“\\” Linux下路径分隔符： “/”
print('获取当前系统的路径分隔符:', os.sep)
# 1.4 获取系统下所有的系统环境变量
print('获取系统下所有的系统环境变量:', os.environ)
print('Linux下获取当前用户:', os.environ.get("USER"))  # Linux下获取当前用户
print('windows下获取当前用户:', os.environ.get("CURRENT_USER_NAME")) # windows下获取当前用户
# 1.5 根据环境变更名称，读取环境变量
print('根据环境变更名称，读取环境变量:', os.getenv("HOSTNAME"))  # Linux下获取计算机名称
print('根据环境变更名称，读取环境变量:', os.getenv("MY_COMPUTER_NAME")) # windows下获取计算机名称
# 1.6 获取cpu数量
print('获取cpu数量:', os.cpu_count())
# 1.7 获取系统详细信息, 适用于Linux操作系统
print('获取系统详细信息:', os.uname())
print('获取系统详细信息:', os.uname().sysname)
print('获取系统详细信息:', os.uname().machine)
# 1.8 获取系统当前的登录用户
print('获取系统当前的登录用户:', os.getlogin())


# 2 os.path
print('----------------------- os.path -----------------------')
# 2.1 获取当前的工作路径
print('获取当前的工作路径:', os.getcwd())  # d:\mycode\pycode
# 2.2 获取文件的绝对路径. 文件存不存在都会返回
print('获取文件的绝对路径:', os.path.abspath(__file__)) # d:\mycode\pycode\demo.py  __file__指当前文件
# 2.3. 将路径分隔为目录和文件名
print('将路径分隔为目录和文件名:', os.path.split("d:/mycode/pycode/demo.py")) # ('d:/mycode/pycode', 'demo.py')
# 2.4 获取文件的目录
print('获取文件的目录:', os.path.dirname("d:/mycode/pycode/demo.py")) # d:/mycode/pycode
# 2.5 获取路径中最后的文件名
print('获取路径中最后的文件名:', os.path.basename("d:/mycode/pycode/demo.py")) # demo.py
# 2.6 路径拼接
print('路径拼接:', os.path.join(os.getcwd(), 'mytest')) # D:\mycode\pycode\mytest
# 2.7 获取路径（文件/文件夹）的最后访问时间
from datetime import datetime
path_atime = os.path.getatime('./01-os模块.py')
print('获取路径（文件/文件夹）的最后访问时间:', datetime.fromtimestamp(path_atime)) # 2022-06-21 10:41:12.095125
# 2.8 获取路径（文件/文件夹）的创建时间
from datetime import datetime
path_ctime = os.path.getctime('./01-os模块.py')
print('获取路径（文件/文件夹）的创建时间:', datetime.fromtimestamp(path_ctime)) # 2022-06-21 10:04:53.622260
# 2.9 获取路径（文件/文件夹）的最后修改时间
from datetime import datetime
path_mtime = os.path.getmtime('./01-os模块.py')
print('获取路径（文件/文件夹）的最后修改时间:', datetime.fromtimestamp(path_mtime)) # 2022-06-21 10:41:12.095125
# 2.10 获取文件大小. 获取路径下文件的内容的大小，为空时返回0， 如果路径不存在，则会报错。
print('获取文件大小:', os.path.getsize('./01-os模块.py')) # 3555
# 2.11 判断是否绝对路径
print('判断是否绝对路径:', os.path.isabs("d:\\mycode\\pycode")) # True
# 2.12 判断文件路径是否存在
print('判断文件路径是否存在:', os.path.exists("d:\\mycode\\pycode\\mylogs")) # False
# 2.13 判断是否文件. 如果被判断的路径不是文件或者路径下文件不存在，则返回False，否则话，返回True
print('判断是否文件:', os.path.isfile("d:/mycode/pycode/mylogs"))  # False
print('判断是否文件: ', os.path.isfile("d:/mycode/pycode/123.py"))  # False
# 2.14 判断是否文件夹. 如果被判断的路径是文件或者文件夹不存在，则返回False。否则返回True.
print('判断是否文件夹:', os.path.isdir("d:/mycode/pycode/demo.py"))  # False
print('判断是否文件夹:', os.path.isdir("d:/mycode/pycode/demo"))  # False
print('判断是否文件夹:', os.path.isdir("d:/mycode/pycode"))  # True
# 2.15 判断用户权限
# F_OK：测试路径的存在。
# R_OK：测试路径的可读性。
# W_OK：测试路径的可写性。
# X_OK：检查是否可以执行路径。
print('判断用户权限:', os.access("./01-os模块.py", os.F_OK | os.R_OK | os.W_OK | os.X_OK)) # False


# 3 文件及文件夹操作
print('----------------------- 文件及文件夹操作 -----------------------')
# 3.1 列出路径下所的文件. 列出路径下所有的文件，并以列表形式返回。
print('列出路径下所的文件:', os.listdir('./')) # ['01-os模块.py', '00-time模块.py']
# 3.2 创建目录
print('创建目录:', os.mkdir("01-os模块test_dir"))
# 判断目录是否存在，如果不存在，创建
# 如果创建的目录存在，会抛出异常。FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。
if not os.path.exists("01-os模块test_dir"): 
    os.mkdir("01-os模块test_dir")

# 3.3 递归创建目录
# 递归创建目录。如果创建的子目录存在，会抛出异常。
# print('递归创建目录:', os.makedirs("d:\\mytest\\test"))
# if not os.path.exists("d:\\mytest\\test"):
#     os.makedirs("d:\\mytest\\test")

# 3.4 删除目录
# 单个删除目录，如果目录不为空，不进行操作
# os.rmdir("d:\\mytest\\test")
# os.rmdir("d:\\mytest")

# 3.5 递归删除
# 归删除目录。 如果子目录成功删除，则removeirs会尝试依次删除路径中显示的每个父目录。如果子目录无法成功删除，则引发OSError。
# os.removedirs("d:\\mytest\\test")
# 3.6 删除文件
# os.remove("d:\\mycode\\pycode\\mytest\\11.py")  # 删除成功
# os.remove("d:\\mycode\\pycode\\mytest")
# 如果删除的内容是一个文件夹抛出异常： PermissionError: [WinError 5] 拒绝访问。

# 3.7 重命名
# os.rename("d:\\mycode\\pycode\\mytest", "d:\\mycode\pycode\\new_test")
# 3.8 为文件添加权限
# os.chmod("c:\\windows\\system32\\drivers\\etc\\hosts", stat.S_IRWXG)
# 序号	    内容	         说明
# 1	    stat.S_ISUID	执行时设置用户ID
# 2	    stat.S_ISGID	执行时设置组ID。
# 3	    stat.S_ENFMT	执行记录锁定。
# 4	    stat.S_ISVTX	执行后保存文本映像
# 5	    stat.S_IREAD	由所有者读取
# 6	    stat.S_IWRITE	由拥有者写入
# 7	    stat.S_IEXEC	由所有者执行
# 8	    stat.S_IRWXU	由所有者读取，写入和执行
# 9	    stat.S_IRUSR	由拥有者读取
# 10	stat.S_IWUSR	由拥有者写入
# 11	stat.S_IXUSR	由所有者执行
# 12	stat.S_IRWXG	按组读取，写入和执行
# 13	stat.S_IRGRP	按组读取
# 14	stat.S_IWGRP	按组写入
# 15	stat.S_IXGRP	按组执行
# 16	stat.S_IRWXO	由其他人读取，写入和执行
# 17	stat.S_IROTH	其他人读取
# 18	stat.S_IWOTH	由他人写
# 19	stat.S_IXOTH	由他人执行
