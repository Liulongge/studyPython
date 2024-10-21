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

# 断言
# 内容的判断机制，如果判断失败，抛出异常
name = "北凡"
assert name == "北凡", "不是北凡"

# 对于测试框架来说：
# 没有异常，判定为通过
# 存在异常，判定为失败

# 用例执行情况
# .         pass        通过
# F         failed      失败(用例执行时报错)
# E         error       出错(fixture执行报错)
# s         skipped     跳过
# X         xpassed     预期外的通过
# x         xfailed     预期内的失败

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

