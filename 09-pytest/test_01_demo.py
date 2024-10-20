# 基本用法
# 测试框架做了什么：
# 1.测试发现
# 2.环境管理
# 3.执行用例
# 4.输出报告

# 测试发现
# 创建test_开头的文件
# 创建Test开头的类
# 创建test_开头的函数或方法

# pytest中以每一个函数或方法，作为一个用例
# pytest主要以名字区分普通函数(方法)、用例
# pytest的启动方式pytest
# pytest输出用例的收集、执行、汇总情况

# 运行
# 1. pytest
# 2. pytest -k [函数]
#       pytest test_01_demo.py::Test::test_b
#       pytest test_01_demo.py::test_a
#        pytest -k test_b

def test_a(): # 函数
    pass

class Test:
    def test_b(self): # 放法
        pass

