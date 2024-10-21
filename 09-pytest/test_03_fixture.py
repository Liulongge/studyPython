# fixture
# 1. fixture的作用范围：支持5级范围
# 2. 同一范围内的用例，共享fixture
# 3. conftest.py 创建全局范围fixture
# 自动的在用例之前、之后完成，用于测试环境的构建和销毁
# 使用“生成器”实现前置、后置的分离


# 运行
# $ pytest
# $ pytest -vs -m ui # -vs 打印详细信息

import pytest

# 方法1
# @pytest.fixture()
# def test():
#     print("\n123\n") # 前置代码，在用例执行之前执行

#     yield

#     print("\nabc\n") # 后置代码，在用例执行之后执行

# # 贴上标记
# @pytest.mark.api
# @pytest.mark.ui
# def test_a(test): # 函数
#     assert 1 == 1 # 测试通过

# class Test:

#     @pytest.mark.api
#     def test_b(self, test):
#         assert 1 == 2

# 方法2, 使用@pytest.mark.usefixtures('test')
# @pytest.fixture()
# def test():
#     print("\n123\n") # 前置代码，在用例执行之前执行

#     yield

#     print("\nabc\n") # 后置代码，在用例执行之后执行

# # 贴上标记
# @pytest.mark.api
# @pytest.mark.ui
# @pytest.mark.usefixtures('test')
# def test_a(): # 函数
#     assert 1 == 1 # 测试通过

# class Test:
#     @pytest.mark.usefixtures('test')
#     @pytest.mark.api
#     def test_b(self):
#         assert 1 == 2

# 3, @pytest.fixture(scope='module'), 整个模块共享
@pytest.fixture(scope='module')
def test():
    print("\n123\n") # 前置代码，在用例执行之前执行

    yield

    print("\nabc\n") # 后置代码，在用例执行之后执行

# 贴上标记
@pytest.mark.api
@pytest.mark.ui
@pytest.mark.usefixtures('test')
def test_a(): # 函数
    assert 1 == 1 # 测试通过

class Test:
    @pytest.mark.usefixtures('test')
    @pytest.mark.api
    @pytest.mark.ui
    def test_b(self):
        assert 1 == 1