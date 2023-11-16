
# 参考： https://blog.csdn.net/mingyuli/article/details/80972135?spm=1001.2014.3001.5506

# python操作文件时，需要打开文件，最后手动关闭文件。
# 通过使用with...as...不用手动关闭文件。当执行完内容后，自动关闭文件。
# with-as表达式极大的简化了每次写finally的工作，这对保持代码的优雅性是有极大帮助的。

# 错误写法
# try:
#     f = open('xxx')
#     do something
# except:
#     do something
# finally:
#     f.close()

# 正确写法：
# try:
#     f = open('xxx')
# except:
#     print 'fail to open'
#     exit(-1)
# try:
#     do something
# except:
#     do something
# finally:
#     f.close()

# 我们为什么要写finally，是因为防止程序抛出异常最后不能关闭文件，但是需要关闭文件有一个前提就是文件已经打开了。 
# 在第一段错误代码中，如果异常发生在f=open(‘xxx’)的时候，比如文件不存在，立马就可以知道执行f.close()是没有意义的。
# 改正后的解决方案就是第二段代码。

# python使用了with-as的语法。当python执行这一句时，会调用__enter__函数，然后把该函数return的值传给as后指定的变量。
# 之后，python会执行下面do something的语句块。最后不论在该语句块出现了什么异常，都会在离开时执行__exit__。 
# 另外，__exit__除了用于tear things down，还可以进行异常的监控和处理，注意后几个参数。

# 在python2.5及以后，file对象已经写好了enter和exit函数，我们可以这样测试：