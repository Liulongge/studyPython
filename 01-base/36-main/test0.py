
# __name__的目的是什么？
# 在执行程序之前，Python解释器将python模块的名称分配给一个名为__name__. 
# 1. __name__等于"main": 将文件作为python脚本执行；
# 2. __name__等于"文件名": 将python文件导入到另一个文件

# eg:
# 1.   python test2.py
# 输出: 
# test1, __name__: __main__
# test1 只有运行该文件才会执行

# 2.   python test0.py
# 输出:
# test1, __name__: test1
# test0 __name__: __main__

# if __name__ == '__main__':
#   main()
# 语句, 只有python脚本作为文件直接调用时,__name__才为main， 内部语句才会被执行
import test1

print('test0 __name__: {}'.format(__name__))

