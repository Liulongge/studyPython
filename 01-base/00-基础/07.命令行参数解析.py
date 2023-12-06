
# argparse是一个用来解析命令行参数的Python库，它是Python标准库的一部分。基于python 2.7的stdlib 代码。
# argparse模块使编写用户友好的命令行界面变得容易。程序定义了所需的参数，而argparse将找出如何从sys.argv(命令行)中解析这些参数。
# argparse模块还会自动生成帮助和使用消息，并在用户为程序提供无效参数时发出错误。

# argparse定义四个步骤：
# 1.导入argparse包 ——import argparse
# 2.创建一个命令行解析器对象 ——创建 ArgumentParser() 对象
# 3.给解析器添加命令行参数 ——调用add_argument() 方法添加参数
# 4.解析命令行的参数 ——使用 parse_args() 解析添加的参数

# 参考: https://blog.csdn.net/craftsman2020/article/details/129237425?spm=1001.2014.3001.5506
# 1、导入argpase包
import argparse 

if __name__ == '__main__':
    # 2、创建参数对象
    parse = argparse.ArgumentParser(description='python命令行解释器学习')
    # 3、往参数对象添加参数  
    parse.add_argument('--param1', type=int, help='第一个int型参数') 
    parse.add_argument('--param2', type=str, help='第一个str型参数')
    # 设置默认参数
    parse.add_argument('--param3', type=str, default='test3', help='设置默认参数')
    # 可选参数引用名
    parse.add_argument('-p', '--param4', type=str, default='test4', help='可选参数引用名')
    # 清除帮助中的参数名信息
    parse.add_argument('-p5', '--param5', type=str, default='test5', metavar='', help='清除帮助中的参数名信息')
    # 清除帮助中的参数名信息
    parse.add_argument('--param6', type=str, default='test6', required=True, help='必选参数')
    
    # 4、解析参数对象获得解析对象
    args = parse.parse_args()  

    print(args.param1, args.param2)
    # 输出coco
