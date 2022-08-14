# 总结：
# import unittest
# 我们运行test_name_function.py时，所有以test_打头的方法都将自动运行。


# 编写函数或类时，还可为其编写测试。通过测试，可确定代码面对各种输入都能够按要求的那样工作。
# 测试让你信心满满，深信即便有更多的人使用你的程序，它也能正确地工作。
# 在程序中添加新代码时，你也可以对其进行测试，确认它们不会破坏程序既有的行为。
# 程序员都会犯错，因此每个程序员都必须经常测试其代码，在用户发现问题前找出它们。

# 1、测试函数
print("========================== 测试函数")
def get_formatted_name(first, last): 
    """Generate a neatly formatted full name.""" 
    full_name = first + ' ' + last 
    return full_name.title()

first = input("\nPlease give me a first name: ") 
last = input("Please give me a last name: ") 

formatted_name = get_formatted_name(first, last) 
print("\tNeatly formatted name: " + formatted_name + '.')

# 单元测试和测试用例
# Python标准库中的模块unittest提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；
# 测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
# 良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。
# 全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
# 对于大型项目，要实现全覆盖可能很难。
# 通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。

# 首先，我们导入了模块unittest和要测试的函数get_formatted_ name()。
# 我们创建了一个名为NamesTestCase的类，用于包含一系列针对get_formatted_name()的单元测试。
# 你可随便给这个类命名，但最好让它看起来与要测试的函数相关，并包含字样Test。
# 这个类必须继承unittest.TestCase类，这样Python才知道如何运行你编写的测试。

# NamesTestCase只包含一个方法，用于测试get_formatted_name()的一个方面。
# 我们运行test_name_function.py时，所有以test_打头的方法都将自动运行。
# 我们使用了unittest类最有用的功能之一：一个断言方法。断言方法用来核实得到的结果是否与期望的结果一致。

# 第1行的句点表明有一个测试通过了。接下来的一行指出Python运行了一个测试，消耗的时间不到0.001秒。
# 最后的OK表明该测试用例中的所有单元测试都通过了。
import unittest

class NamesTestCase(unittest.TestCase): 
    """测试name_function.py""" 
    def test_first_last_name(self): 
        """能够正确地处理像Janis Joplin这样的姓名吗？""" 
        formatted_name = get_formatted_name('janis', 'joplin') 
        self.assertEqual(formatted_name, 'Janis Joplin') 

unittest.main()
