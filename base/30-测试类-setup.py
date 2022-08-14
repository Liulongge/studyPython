# 总计：
# setup()
# 在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。

# 运行测试用例时，每完成一个单元测试，Python都打印一个字符：测试通过时打印一个
# 句点；测试引发错误时打印一个E；测试导致断言失败时打印一个F。

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