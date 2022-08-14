

# 在本章前半部分，你编写了针对单个函数的测试，下面来编写针对类的测试。
# 很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。
# 如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。

# Python在unittest.TestCase类中提供了很多断言方法。
# 前面说过，断言方法检查你认为应该满足的条件是否确实满足。
# 如果该条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。
# 如果你认为应该满足的条件实际上并不满足，Python将引发异常。

# unittest Module中的断言方法
# 方 法 用 途
# assertEqual(a, b)        核实 a == b
# assertNotEqual(a, b)     核实 a != b
# assertTrue(x)            核实x为 True
# assertFalse(x)           核实x为 False
# assertIn(item, list)     核实item在list中
# assertNotIn(item, list)  核实item不在list中
print("========================== 测试类")
class AnonymousSurvey(): 
    """收集匿名调查问卷的答案""" 
    def __init__(self, question): 
        """存储一个问题，并为存储答案做准备""" 
        self.question = question 
        self.responses = [] 
    def show_question(self): 
        """显示调查问卷""" 
        print(question) 
    def store_response(self, new_response): 
        """存储单份调查答卷""" 
        self.responses.append(new_response) 
    def show_results(self): 
        """显示收集到的所有答卷""" 
        print("Survey results:") 
        for response in self.responses: 
            print('- ' + response)

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?" 
my_survey = AnonymousSurvey(question) 
#显示问题并存储答案
my_survey.show_question() 
print("Enter 'q' at any time to quit.\n") 
response = input("Language: ") 
my_survey.store_response(response) 
# 显示调查结果
print("Thank you to everyone who participated in the survey!") 
my_survey.show_results()

# 测试 AnonymousSurvey 类
import unittest
class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试""" 
    def test_store_single_response(self): 
        """测试单个答案会被妥善地存储""" 
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English') 
        self.assertIn('English', my_survey.responses) 

unittest.main()


# 方法 setUp()
print("========================== 方法 setUp()")
# 如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
# 这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。
import unittest 

class TestAnonymousSurvey(unittest.TestCase): 
    """针对AnonymousSurvey类的测试""" 
    def setUp(self): 
        """ 创建一个调查对象和一组答案，供使用的测试方法使用 """ 
        question = "What language did you first learn to speak?" 
        self.my_survey = AnonymousSurvey(question) 
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self): 
        """测试单个答案会被妥善地存储""" 
        self.my_survey.store_response(self.responses[0]) 
        self.assertIn(self.responses[0], self.my_survey.responses) 
    
    def test_store_three_responses(self): 
        """测试三个答案会被妥善地存储""" 
        for response in self.responses: 
            self.my_survey.store_response(response) 
        for response in self.responses: 
            self.assertIn(response, self.my_survey.responses) 

unittest.main()