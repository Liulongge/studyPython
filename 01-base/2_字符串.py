

# 1. 在字符串中包含引号和撇号
print('I told my friend, "Python is my favorite language!"')

# 2. 使用方法修改字符串的大小写
# title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写
name = "ada lovelace"
print(name.title())

# 将字符串改为全部大写或全部小写
# 方法lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。
# 以后需要显示这些信息时，再将其转换为最合适的大小写方式。
name = "Ada Lovelace"
print(name.upper()) # 全大写
print(name.lower()) # 全小写

# 3. 合并（拼接）字符串
# python中使用 + 号来完成字符串拼接
# 这种合并字符串的方法称为拼接 。通过拼接，可使用存储在变量中的信息来创建完整的消息

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " + " + last_name
print(full_name)

# 可以使用拼接来创建消息，再把整条消息都存储在一个变量中
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# 4. 使用制表符或换行符来添加空白
# 要在字符串中添加换行符，可使用字符组合\n
# 要在字符串中添加制表符，可使用字符组合\t
# 还可在同一个字符串中同时包含制表符和换行符。字符串"\n\t" 让Python换到下一行，并在下一行开头添加一个制表符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 5. 删除空白
# 在程序中，额外的空白可能令人迷惑。对程序员来说，'python' 和'python ' 看起来几乎没什么两样，但对程序来说，它们却是两个不同的字符串
# Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法rstrip() 。
# 对变量favorite_language 调用方法rstrip() 后，这个多余的空格被删除了。然而，这种删除只是暂时的，接下来再次询问favorite_language 的值时，
# 会发现这个字符串与输入时一样，依然包含多余的空白。
# 要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中：
favorite_language = '    python   '
print(favorite_language)
print('"rstrip: "', favorite_language.rstrip())
print('"lstrip: "', favorite_language.lstrip())
print('"strip: "', favorite_language.strip())
favorite_language = favorite_language.strip()
print(favorite_language)


# 5. 使用函数str() 避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)


# 彩色打印
