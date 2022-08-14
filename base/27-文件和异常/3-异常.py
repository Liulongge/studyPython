
# 总结：
# 异常：ZeroDivisionError、FileNotFoundError
# try - except
# try - except - else

# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知所措的错误时，它都会创建一个异常对象。
# 如果你编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
# 异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
# 使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback。

# 1、处理 ZeroDivisionError 异常
print("========================== 处理 ZeroDivisionError 异常")
# print(5/0)

# 2、使用 try-except 代码块
print("========================== try-except")
# 当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。
# 你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。
# 处理ZeroDivisionError异常的try-except代码块类似于下面这样：

# 我们将导致错误的代码行print(5/0)放在了一个try代码块中。如果try代码块中的代码运行起来没有问题，
# Python将跳过except代码块；如果try代码块中的代码导致了错误，Python将查找这样的except代码块，并运行其中的代码，
# 即其中指定的错误与引发的错误相同。
# 在这个示例中，try代码块中的代码引发了ZeroDivisionError异常，因此Python指出了该如何解决问题的except代码块，并运行其中的代码。
# 这样，用户看到的是一条友好的错误消息，而不是traceback：
try: 
    print(5/0) 
except ZeroDivisionError: 
    print("You can't divide by zero!")


# 3、使用异常避免崩溃
print("========================== 使用异常避免崩溃 try-except-else")
# 发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。
# 这种情况经常会出现在要求用户提供输入的程序中；
# 如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。
# 下面来创建一个只执行除法运算的简单计算器：

# 通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。
# 错误是执行除法运算的代码行导致的，因此我们需要将它放到try-except代码块中。
# 这个示例还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：

# try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；
# 只有可能引发异常的代码才需要放在try语句中。
# 有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。
# except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。
# 通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。

print("Give me two numbers, and I'll divide them.") 

first_number = input("\nFirst number: ") 
second_number = input("Second number: ") 
try: 
    answer = int(first_number) / int(second_number) 
except ZeroDivisionError: 
    print("You can't divide by 0!") 
else: 
    print(answer)


# 4、处理 FileNotFoundError 异常
print("========================== 处理 FileNotFoundError 异常")
# 使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。
# 对于所有这些情形，都可使用try-except代码块以直观的方式进行处理。
# 我们来尝试读取一个不存在的文件。下面的程序尝试读取文件alice.txt的内容，但我没有将这个文件存储在alice.py所在的目录中：
# 在这个示例中，try代码块引发FileNotFoundError异常，因此Python找出与该错误匹配的except代码块，并运行其中的代码。
# 最终的结果是显示一条友好的错误消息，而不是traceback：
filename = 'alice2.txt'

try: 
    with open(filename) as f_obj: 
        contents = f_obj.read() 
except FileNotFoundError: 
    msg = "Sorry, the file " + filename + " does not exist." 
    print(msg)

# 5、分析文本
print("========================== 分析文本")
# 你可以分析包含整本书的文本文件。很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。
# 下面来提取童话Alice in Wonderland的文本，并尝试计算它包含多少个单词。
# 我们将使用方法split()，它根据一个字符串创建一个单词列表。下面是对只包含童话名"Alice in Wonderland"的字符串调用方法split()的结果。
# 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
# 结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。为计算Alice in Wonderland包含多少个单词，
# 我们将对整篇小说调用split()，再计算得到的列表包含多少个元素，从而确定整篇童话大致包含多少个单词：

# 我们把文件alice.txt移到了正确的目录中，让try代码块能够成功地执行。
# 我们对变量contents调用方法split()，以生成一个列表，其中包含这部童话中的所有单词。
# 当我们使用len()来确定这个列表的长度时，就知道了原始字符串大致包含多少个单词。
# 我们打印一条消息，指出文件包含多少个单词。这些代码都放在else代码块中，因为仅当try代码块成功执行时才执行它们。
# 输出指出了文件alice.txt包含多少个单词：

filename = 'alice.txt' 
try: 
    with open(filename) as f_obj: 
        contents = f_obj.read() 
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist." 
    print(msg) 
else: 
    # 计算文件大致包含多少个单词
    words = contents.split() 
    num_words = len(words) 
    print("The file " + filename + " has about " + str(num_words) + " words.")

# 6、使用多个文件
# 现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。
# 为此，我们将要分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用count_words()。
# 我们将尝试计算Alice in Wonderland、Siddhartha、Moby Dick和Little Women分别包含多少个单词，它们都不受版权限制。
# 我故意没有将siddhartha.txt放到word_count.py所在的目录中，让你能够看到这个程序在文件不存在时处理得有多出色：

# 使用try-except代码块提供了两个重要的优点：避免让用户看到traceback；
# 让程序能够继续分析能够找到的其他文件。如果不捕获因找不到siddhartha.txt而引发的FileNotFoundError异常，
# 用户将看到完整的traceback，而程序将在尝试分析Siddhartha后停止运行——根本不分析Moby Dick和Little Women。
print("========================== 使用多个文件")
def count_words(filename): 
    """计算一个文件大致包含多少个单词""" 
    try: 
        with open(filename) as f_obj: 
            contents = f_obj.read() 
    except FileNotFoundError: 
        msg = "Sorry, the file " + filename + " does not exist." 
        print(msg) 
    else: 
        # 计算文件大致包含多少个单词
        words = contents.split() 
        num_words = len(words) 
        print("The file " + filename + " has about " + str(num_words) + " words.") 

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
for filename in filenames: 
    count_words(filename)

# 7、失败时一声不吭
print("========================== 失败时一声不吭/决定报告哪些错误")