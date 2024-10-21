# 高级语法
# 1.mark
#   标记是为了用例之间彼此不同，实现用例筛选
#   标记的使用步骤：
#       1.注册标记: pytest.ini文件
#       2.贴上标记: @pytest.mark.api, 一个用例可以打上不同标记
#       3.筛选标记: 
#           pytest -m api           # 筛选单个标记
#           pytest -m "api or e2e"  # 筛选多个标记
#           pytest -m "api and e2e" # 筛选多个标记
#   除了自己注册的标记之外，pytest还内置了一些标记：跳过、预期失败、参数化、调用fixture
#   第三方插件，也会内置一些标记：执行顺序、执行依赖、失败重试

import pytest

# 贴上标记
@pytest.mark.api
def test_a(): # 函数
    assert 1==1 # 测试通过

class Test:

    @pytest.mark.api
    @pytest.mark.e2e
    def test_b(self):
        assert 1 == 2

