
# 总结：
# 1、读取文件：
# with open(“文件名”) as file :
#     contents = file.read()        
# 2、逐行读取
# with open("文件名") as file :
#     lines = file.readlines() 
# 文件内容仅在with代码块内有效，可将内容存于列表，在外部访问
# 
# 3、注意：open之后，python会自动关闭文件
# 文件每行的末尾都有一个看不见的换行符，使用strip可将其删除


# 从文件中读取数据
# 文本文件可存储的数据量多得难以置信：天气数据、交通数据、社会经济数据、文学作品等。
# 每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其
# 如此。例如，你可以编写一个这样的程序：读取一个文本文件的内容，重新设置这些数据的格式
# 并将其写入文件，让浏览器能够显示这些内容。

# 1、读取整个文件
print("========================== 读取整个文件")
# 我们先来看看函数open()。要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开文件，这样才能访问它。
# 函数open()接受一个参数：要打开的文件的名称。
# 函数open()返回一个表示文件的对象。在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象；
# Python将这个对象存储在我们将在后面使用的变量中。
# 关键字with在不再需要访问文件后将其关闭。
# 你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。
with open('pi_digits.txt') as file_object: 
    contents = file_object.read() 
    print(contents)

# 2、文件路径
print("========================== 文件路径件")
# Windows系统有时能够正确地解读文件路径中的斜杠。如果你使用的是Windows系统，且
# 结果不符合预期，请确保在文件路径中使用的是反斜杠。

# 3、逐行读取
print("========================== 逐行读取")
# 读取文件时，常常需要检查其中的每一行：你可能要在文件中查找特定的信息，或者要以
# 某种方式修改文件中的文本。
# 每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符，
# 因此每行末尾都有两个换行符：一个来自文件，另一个来自print语句。要消除这些多余的空白行，可在print语句中使用rstrip()：
filename = 'pi_digits.txt' 
with open(filename) as file_object: 
    for line in file_object: 
        print(line.strip())

# 4、创建一个包含文件各行内容的列表
print("========================== 创建一个包含文件各行内容的列表")
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外
# 访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该
# 列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
filename = 'pi_digits.txt' 
with open(filename) as file_object: 
    lines = file_object.readlines() 

# 法readlines()从文件中读取每一行，并将其存储在一个列表中；接下来，该列表被存储到变量lines中；
# 在with代码块外，我们依然可以使用这个变量。我们使用一个简单的for循环来打印lines中的各行。
# 由于列表lines的每个元素都对应于文件中的一行，因此输出与文件内容完全一致。
for line in lines: 
    print(line.rstrip())


# 5、使用文件的内容
# 将文件读取到内存中后，就可以以任何方式使用这些数据了。下面以简单的方式使用圆周率的值。
# 首先，我们将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格：
# 注意 读取文本文件时，Python将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，
# 就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数。
print("========================== 使用文件的内容")
filename = 'pi_digits.txt'
with open(filename) as file_object: 
    lines = file_object.readlines() 

pi_string = '' 
for line in lines: 
    pi_string += line.strip() 

print(pi_string) 
print(len(pi_string))

# 6、包含一百万位的大型文件
print("========================== 包含一百万位的大型文件")
# 前面我们分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文件。
# 如果我们有一个文本文件，其中包含精确到小数点后1 000 000位而不是30位的圆周率值，也可
# 创建一个包含所有这些数字的字符串。为此，我们无需对前面的程序做任何修改，只需将这个
# 文件传递给它即可。在这里，我们只打印到小数点后50位，以免终端为显示全部1 000 000位而不断地翻滚：
filename = 'pi_million_digits.txt' 
with open(filename) as file_object: 
    lines = file_object.readlines() 

pi_string = '' 
for line in lines: 
    pi_string += line.strip() 

print(pi_string[:100] + "...") 
print(len(pi_string))

# 7、圆周率值中包含你的生日吗
print("========================== 圆周率值中包含你的生日吗")
filename = 'pi_million_digits.txt' 
with open(filename) as file_object: 
    lines = file_object.readlines()

pi_string = '' 
for line in lines: 
    pi_string += line.strip() 
print(pi_string[:100] + "...") 

birthday = input("Enter your birthday, in the form mmddyy: ") 
if birthday in pi_string: 
    print("Your birthday appears in the first million digits of pi!") 
else: 
    print("Your birthday does not appear in the first million digits of pi.")