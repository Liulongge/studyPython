
# Python内置变量是指在Python解释器启动时就已经存在的变量，它们可以在任何地方直接使用，无需导入或定义。
# __name__: 这是一个字符串变量，表示当前模块的名称。
# 如果当前模块是主程序，那么它的值是`'__main__'`，否则是模块的文件名（不含后缀）
# 输出: __name__: __main__
print("__name__: {}".format(__name__))

# __doc__: 这是一个字符串变量，表示当前模块的文档字符串。
# 如果当前模块有以三引号开头和结尾的注释，那么它的值就是这段注释的内容，否则是`None`
# 这个变量常用于生成文档或帮助信息
# 输出: __doc__: None
print("__doc__: {}".format(__doc__))

# __file__: 这是一个字符串变量，表示当前模块的绝对路径。
# 如果当前模块是交互式环境或内置模块，那么它的值是`None`。
# 这个变量常用于获取当前模块所在的目录或文件名。
# 输出: __file__: /Users/xxx/01-base/37-python内置变量.py
print("__file__: {}".format(__file__))

# __package__: 这是一个字符串变量，表示当前模块所属的包名。
# 如果当前模块是顶级模块或主程序，那么它的值是`None`，否则是包的全名。
# 这个变量常用于相对导入
# 输出: __package__: None
print("__package__: {}".format(__package__))

# __builtins__: 这是一个模块对象，表示Python的内置模块`builtins`，它包含了Python的所有内置函数和异常类。
# 这个变量可以省略，直接使用内置函数或异常类的名称
# 输出: __builtins__: <module 'builtins' (built-in)>
print("__builtins__: {}".format(__builtins__))

# __dict__: 这是一个字典对象，表示当前模块的命名空间，它包含了当前模块中定义的所有变量和函数。
# 这个变量可以用于动态访问或修改当前模块的属性
# print("__dict__: {}".format(__dict__))

# 获取函数行号
import inspect
print('获取函数行号: {}'.format(inspect.currentframe ().f_lineno))
import sys
print('获取函数行号: {}'.format(sys._getframe ().f_lineno))